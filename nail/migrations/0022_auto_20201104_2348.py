# Generated by Django 3.1.2 on 2020-11-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0021_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='url',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='picture',
            field=models.ImageField(upload_to='services/', verbose_name='Фотография'),
        ),
    ]
