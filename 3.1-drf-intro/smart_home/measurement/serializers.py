from .models import Sensor, Measurement
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "location"]

        
        
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id", "temperature", "created_at", "sensor"]


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "location", "measurement"]