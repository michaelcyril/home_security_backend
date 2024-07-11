from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *


class IntruderRequestsView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        serialized = IntruderAttemptSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
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
        # data = request.data
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
        return Response({"complete": True})

    @staticmethod
    def get(request):
        queryset = Sensor.objects.all()
        return Response(SensorSerializer(instance=queryset, many=True).data)