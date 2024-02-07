from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sensor_management.models import *

class SensorRequestsView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        print(data)
        data = Reading.objects.create(
            pir1 = data['PIR1'],
            pir2 = data['PIR2'],
            pir3 = data['PIR3'],
            pir4 = data['PIR4'],
            status = data['Buz']
        )
        data.save()
        return Response({"send": True})

    @staticmethod
    def get(request):
        try:
            data = Reading.objects.values('id', 'trigger', 'pir1', 'pir2', 'pir3', 'pir4', 'status').filter(trigger=1)[0]
        except:
            data = Reading.objects.values('id', 'trigger', 'pir1', 'pir2', 'pir3', 'pir4', 'status').all()[0]
        return Response(data)

class TriggerActionView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            object = Reading.objects.all()[0]
            object.trigger = 1
            object.save()
        except:
            object = []
        return Response({"status": True})


class TriggerActionOffView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        try:
            object = Reading.objects.filter(trigger=1)[0]
            object.trigger = 2
            object.save()
        except:
            object = []
        return Response({"status": True})

# {
#     "trigger": True
# }


