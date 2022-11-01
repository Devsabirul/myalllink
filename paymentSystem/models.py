from email.policy import default
from random import choices
from django.db import models

# Create your models here.


class PaymentModel(models.Model):
    PAYMENT_METHOD = (
        ('Paypal', 'Paypal'),
        ('SSLcommerz', 'SSLcommerz'),
    )
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD, default='Paypal')
