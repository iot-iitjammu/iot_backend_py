from django.urls import path
from .views import OktaAuthView

urlpatterns = [
    path('okta/callback', OktaAuthView.as_view())
]
