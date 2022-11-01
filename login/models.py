from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='Friends', blank=True)
    avatar = models.ImageField(upload_to='profilePicture', blank=True)
