from django.db import models

# Create your models here.
class ElectricalData(models.Model):
    client_id = models.CharField(max_length=100)
    voltage_rms = models.FloatField()
    current_rms = models.FloatField()
    average_power = models.FloatField()
    energy_consumption = models.FloatField()
    generation_time_stamp = models.IntegerField()
    delete_status = models.BooleanField()

