from django.urls import path
from electrical_logger.views import PopulateElectricalData

urlpatterns = [
    path('populateDummyData', PopulateElectricalData.as_view()),
]
