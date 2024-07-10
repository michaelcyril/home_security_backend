from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *


class SensorRequestsView(APIView):
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
        return Response(IntruderAttemptSerializer(instance=queryset).data)


class TriggerAction(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        return Response({"status": data['status'], "PIR": data['PIR']})

# {
#     "status": "ON",
#     "PIR": 1
# }
