# Generated by Django 3.1.2 on 2020-11-02 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0019_reserv_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Заявка подана'),
        ),
    ]
