# Generated by Django 4.1.3 on 2023-01-03 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0032_historialobject_accountreceiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialobject',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 14, 21, 43, 40354)),
        ),
        migrations.AlterField(
            model_name='historialobjectreceived',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 14, 21, 43, 42054)),
        ),
    ]
