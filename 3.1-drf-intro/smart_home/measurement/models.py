from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='датчик')
    location = models.CharField(max_length=100, verbose_name='расположение')
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    
class Measurement(models.Model):
    id = models.ForeignKey(Sensor, unique=True, primary_key=True, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='температура')
    date = models.DateField(verbose_name='дата измерения', auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'