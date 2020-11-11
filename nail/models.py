from time import timezone

from django.db import models
from django.urls import reverse
from datetime import datetime
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField


class Header(models.Model):
    title = models.CharField('Название', max_length=20, blank=True)
    description = models.CharField('Описание', max_length=20)
    content = models.TextField('Содержание', max_length=250)
    insta = models.CharField('Инстаграм', max_length=100, blank=True)
    facebook = models.CharField('Фейсбук', max_length=100, blank=True)
    telegram = models.CharField('Телеграм', max_length=100, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная страница(шапка)'
        verbose_name_plural = 'Главная страница(шапка)'

    def get_services(self):
        services = Services.objects.all()
        return services


class Reserv(models.Model):
    name = models.CharField('Имя', max_length=30)
    phone = models.CharField('Номер телефона', max_length=15)
    time = models.DateField('Запись на число', default=datetime.now, blank=True, null=True)
    create_time = models.DateTimeField('Заявка подана', default=datetime.now, blank=True, null=True)
    description = models.TextField('Доп.инфо', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Services(models.Model):
    name = models.CharField('Название', max_length=20)
    content = models.TextField('Описание', max_length=5000)
    picture = models.ImageField('Фотография', upload_to='services/')
    url = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('services', kwargs={"slug": self.url})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)

        if img.height > 100 or img.weight > 100:
            output_size = (400,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

class PriceList(models.Model):
    name = models.CharField('Название', max_length=40)
    description = models.TextField('Описание', max_length=80, blank=True)
    cash = models.CharField('Цена или другое', max_length=40, blank=True)
    service = models.ForeignKey(Services, verbose_name='Услуга', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'

class Pages(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=200, blank=True)
    content = models.TextField('Контент', max_length=5000)
    url = models.SlugField(max_length=100, unique=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'