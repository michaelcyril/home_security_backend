from rest_framework import serializers
from sensor_management.models import *


class IntruderAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntruderAttempt
        fields = ['id', 'trigger', 'pir', 'status', 'created_at']
