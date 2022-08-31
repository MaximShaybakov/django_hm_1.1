from django.contrib import admin
from .serializers import SensorSerializer, MeasurementSerializer

# Register your models here.
@admin.register(SensorSerializer)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']
    
    class Meta:
        verbose_name = 'сенсор'
        verbose_name_plural = 'сенсоры'
        
        
@admin.register(MeasurementSerializer)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'date']
    
    class Meta:
        verbose_name = 'измерение'
        verbose_name_plural = 'измерения'