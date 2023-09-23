from django.urls import path

from .views import DeviceCreateAPI, DeviceDetailAPI

urlpatterns = [
    path("devices/", DeviceCreateAPI.as_view(), name="create_device"),
    path("devices/id<pk>/", DeviceDetailAPI.as_view(), name="device_detail"),
]
