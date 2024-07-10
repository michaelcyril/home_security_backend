from django.urls import path
from .views import *
app_name = 'sensor_management'

urlpatterns = [
    path('sensor-request', SensorRequestsView.as_view()),
    path('trigger-action', TriggerAction.as_view()),
]
