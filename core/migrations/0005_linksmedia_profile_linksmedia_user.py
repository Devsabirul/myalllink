# Generated by Django 4.1.2 on 2022-11-01 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_profile_avatar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_rename_iamge_linksmedia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksmedia',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.profile'),
        ),
        migrations.AddField(
            model_name='linksmedia',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
