from django.conf.urls import url
from django.urls import path, include
from dashboard.views import PowerHistogramView

urlpatterns = [
    path('powerHistogram/', PowerHistogramView.as_view()),
]
