# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from urllib import request
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView



class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    
    
class SensorView_Update(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
    
class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
    

class MeasurementView_Create(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer