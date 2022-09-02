from django.urls import path
from .views import SensorView, MeasurementView, SensorView_Update

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view(), name='smart_home'),
    path('sensor/<int:pk>/', SensorView_Update.as_view()),
    path('measurements/', MeasurementView.as_view())
    
]