# Generated by Django 3.1.2 on 2020-11-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0010_auto_20201102_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
    ]
