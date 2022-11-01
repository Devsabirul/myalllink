from django.db import models
from django.contrib.auth.models import User
from login.models import *


# Create your models here.


class Linksmedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    weblink = (
        ('Web Link', 'Web Link'),
        ('Facebook', 'Facebook'),
        ('Youtube', 'Youtube'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Linkedin', 'Linkedin'),
        ('Tik Tok', 'Tik Tok'),
        ('DropBox', 'DropBox'),
        ('Pinterest', 'Pinterest'),
        ('NGL', 'NGL'),
        ('Discord', 'Discord'),
        ('OnlyFans', 'OnlyFans'),
    )
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True, null=True)
    icon = models.CharField(
        max_length=50, choices=weblink, default='Web Link')
    image = models.ImageField(upload_to="images/")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
