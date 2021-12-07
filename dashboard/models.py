from django.db import models

# Create your models here.
class ElectricalData(models.Model):
    client_id = models.CharField(max_length=100)
    generation_time_stamp = models.IntegerField()
    voltage_rms = models.FloatField()
    current_rms = models.FloatField()
    voltage_peak = models.FloatField()
    current_peak = models.FloatField()
    phase = models.FloatField()
    voltage_frequency = models.FloatField()
    average_power = models.FloatField()
    energy_consumption = models.FloatField()
    delete_status = models.BooleanField()
