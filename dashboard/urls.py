from django.conf.urls import url
from django.urls import path, include
from .api.GetHistogram import PowerHistogramView

urlpatterns = [
    path('powerHistogram/', PowerHistogramView.as_view()),
]