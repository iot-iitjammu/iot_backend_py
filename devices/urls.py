from django.urls import path
from devices.views import DeviceStatus

urlpatterns = [
    path('allClients', DeviceStatus.as_view())
]
