# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from urllib import request
from .serializers import SensorSerializer, MeasurementSerializer
from .models import Sensor, Measurement
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView



class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class SensorView_Retr(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class =SensorSerializer
    

class SensorView_Create(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class SensorView_Update(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class MeasurementView_Create(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer