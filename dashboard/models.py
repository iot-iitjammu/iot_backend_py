# from django.db import models
from mongoengine import Document
import mongoengine.fields as models

# Create your models here.
class ElectricalData(Document):
    client_id = models.StringField()
    timestamp = models.IntField()
    voltage_rms = models.FloatField()
    current_rms = models.FloatField()
    voltage_peak = models.FloatField()
    current_peak = models.FloatField()
    phase = models.FloatField()
    voltage_frequency = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    delete_status = models.BooleanField()
