from django.urls import path
from .views import *
app_name = 'sensor_management'

urlpatterns = [
    path('create-get-intruder-attempt', IntruderRequestsView.as_view()),
    path('trigger-action', TriggerAction.as_view()),
    path('create-get-sensor', CreateGetSensorView.as_view()),
]
