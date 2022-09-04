from django.urls import path
from .views import MeasurementView_Create, SensorView, MeasurementView, SensorView_Update

urlpatterns = [
    path('sensor/', SensorView.as_view(), name="smart_home"),
    path('sensor/<int:pk>/', SensorView_Update.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurement/<int:pk>/', MeasurementView_Create.as_view())    
]