from django.urls import path
from .views import *
urlpatterns = [
    path('', login_, name="Login"),
    path('signup', registration, name="registration"),
    path('logout', logout_, name="logout"),
]
