# Generated by Django 3.1.2 on 2020-11-10 17:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nail', '0027_auto_20201108_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AddField(
            model_name='pages',
            name='code',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]