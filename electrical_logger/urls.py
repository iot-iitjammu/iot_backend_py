from django.urls import path
from electrical_logger.views import PopulateElectricalData, LogElectricalData

urlpatterns = [
    path('populateDummyData/', PopulateElectricalData.as_view()),
    path('logElectricalData/', LogElectricalData.as_view()),
]
