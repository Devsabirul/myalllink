from django.shortcuts import render
from paymentSystem.forms import *
# Create your views here.


def paymentSystem(request):

    payment_method = PaymentSystemMethod()
    context = {
        'paymentmethod': payment_method
    }
    return render(request, 'payment/index.html', context)
