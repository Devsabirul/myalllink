# Generated by Django 4.1.2 on 2022-10-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksmedia',
            name='icon',
            field=models.CharField(choices=[('Web Link', 'Web Link'), ('Facebook', 'Facebook'), ('Youtube', 'Youtube'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Linkedin', 'Linkedin'), ('Tik Tok', 'Tik Tok'), ('DropBox', 'DropBox'), ('Pinterest', 'Pinterest'), ('NGL', 'NGL'), ('Discord', 'Discord'), ('OnlyFans', 'OnlyFans')], default='Web Link', max_length=50),
        ),
    ]
