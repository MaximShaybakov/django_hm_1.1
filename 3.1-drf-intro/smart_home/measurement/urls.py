from django.urls import path
from .views import SensorView, SensorView_Retr, SensorView_Create, SensorView_Update, MeasurementView_Create

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('sensor/<int:pk>/', SensorView_Retr.as_view()),
    path('sensors/', SensorView_Create.as_view()),
    path('sensors/<int:pk>/', SensorView_Update.as_view()),
    path('measurements/', MeasurementView_Create.as_view()),
    
]