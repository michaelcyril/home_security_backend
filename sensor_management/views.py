from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import api_view


class IntruderRequestsView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        raw_data_key = list(request.data.keys())[0]
        data_separation = raw_data_key.split("_")
        if len(data_separation) != 2:
            return Response({"send": False, "error": "Invalid data"})
        if data_separation[0] != "normal":
            data = {
                "pir": data_separation[0],
                "status": data_separation[1]
            }
            # print(data_separation[0])
            # print("status", data_separation[1])

            serialized = IntruderAttemptSerializer(data=data)
            if serialized.is_valid():
                # serialized.save()
                # alarm.
                print("saved==========")
                return Response({"send": True})
        else:
            print("normal status ", data_separation[1])
            alarm = Alarm.objects.all()[0]
            alarm.normal_status = data_separation[1]
            alarm.save()
            return Response({"send": True})
        return Response({"send": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = IntruderAttempt.objects.all()
        return Response(IntruderAttemptSerializer(instance=queryset, many=True).data)


class TriggerAction(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        pir = data['PIR']
        try:
            sensor = Sensor.objects.get(pir=pir)
            sensor.status = data['status']
            sensor.save()
            queryset = Alarm.objects.all()
            if len(queryset) == 0:
                Alarm.objects.create(status=0)
            queryset = Alarm.objects.all()
            queryset[0].status = data['status']
            queryset[0].save()
            return Response({"send": True})
        except Sensor.DoesNotExist:
            return Response({"send": False, "error": "Sensor not found"})


# {
#     "status": 1,
#     "PIR": "PIR1"
# }


class CreateGetSensorView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        queryset = Sensor.objects.all()
        if len(queryset) == 0:
            pirs = ["PIR1", "PIR2", "PIR3", "PIR4"]
            for pir in pirs:
                data = {
                    "pir": pir,
                    "status": 0
                }
                serialized = SensorSerializer(data=data)
                if serialized.is_valid():
                    serialized.save()
                    print(f'SAVE: {pir}')
                else:
                    print(f'ERROR: {pir}')
        return Response({"status": 1})

    @staticmethod
    def get(request):
        queryset = Sensor.objects.all()
        return Response(SensorSerializer(instance=queryset, many=True).data)


class ActivateDeactivateAlarm(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        queryset = Alarm.objects.all()
        if len(queryset) < 1:
            Alarm.objects.create(status=0)
        queryset = Alarm.objects.all()[0]
        if queryset.status == 1:
            queryset.status = 0
            queryset.save()
        else:
            queryset.status = 1
            queryset.save()
        return Response({"status": queryset.status})

@api_view()
def getAlarmView(request):
    queryset = Alarm.objects.all()
    if len(queryset) < 1:
        Alarm.objects.create(status=0)
    queryset = Alarm.objects.all()[0]
    return Response(f"status*{queryset.status}={queryset.normal_status}")

# {
#     "status": 1,
#     "PIR": "PIR1"
# }
