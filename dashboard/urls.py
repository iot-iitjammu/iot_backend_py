from django.conf.urls import url
from django.urls import path, include
from dashboard.views import PowerHistogramView, EnergyHistogramView

urlpatterns = [
    path('powerHistogram', PowerHistogramView.as_view()),
    path('energyHistogram', EnergyHistogramView.as_view()),
]
