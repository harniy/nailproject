# Generated by Django 3.1.2 on 2020-10-28 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('content', models.TextField(max_length=10000, verbose_name='Контент')),
                ('picture', models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка')),
                ('url', models.SlugField(default='', max_length=150)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nail.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Страницы',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
