from rest_framework import serializers
from sensor_management.models import *


class IntruderAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntruderAttempt
        fields = ['id', 'pir', 'status', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'pir', 'status', 'created_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'phone_number', 'server_ip', 'email']
