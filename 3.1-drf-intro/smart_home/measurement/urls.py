from django.urls import path
from .views import SensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view(), name='сенсоры'),
    path('sensor/<pk>', SensorView.as_view(), name='сенсор'),
    path('meassurement/', MeasurementView.as_view(), name='измерения')
    
]
