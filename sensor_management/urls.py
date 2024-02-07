from django.urls import path
from .views import *
app_name = 'sensor_management'

urlpatterns = [
    path('requests', SensorRequestsView.as_view()),
    path('trigger-on', TriggerActionView.as_view()),
    path('trigger-off', TriggerActionOffView.as_view()),
]
