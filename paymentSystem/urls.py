from django.urls import path
from .views import *

urlpatterns = [
    path('', paymentSystem, name="paymentSystem")
]
