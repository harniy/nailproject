# Generated by Django 3.1.2 on 2020-11-01 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0008_auto_20201031_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Доп.инфо')),
            ],
        ),
    ]
