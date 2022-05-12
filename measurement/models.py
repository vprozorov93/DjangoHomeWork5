from django.db import models


class Sensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name + f' "{self.description}"'


class Measurement(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Показания'
        verbose_name_plural = 'Показание'

