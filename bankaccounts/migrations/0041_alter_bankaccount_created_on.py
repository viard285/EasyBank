# Generated by Django 4.1.3 on 2023-01-03 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0040_alter_bankaccount_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 13, 6, 9, 841430)),
        ),
    ]
