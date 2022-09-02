from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    location = models.CharField(max_length=100, verbose_name='location')
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    
class Measurement(models.Model):
    temperature = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='temperature')
    created_at = models.DateField(verbose_name='created_at', auto_now=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    
    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'