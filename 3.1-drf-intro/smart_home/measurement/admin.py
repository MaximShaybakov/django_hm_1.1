from django.contrib import admin
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location"]
        
        
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ["id", "temperature", "created_at", "sensor"]