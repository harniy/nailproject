# Generated by Django 3.1.2 on 2020-11-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0013_auto_20201102_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv',
            name='time',
            field=models.DateField(blank=True),
        ),
    ]
