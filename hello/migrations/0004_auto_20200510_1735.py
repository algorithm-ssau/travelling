# Generated by Django 3.0.4 on 2020-05-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200510_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='im',
            field=models.ImageField(blank=True, help_text='380x250px', null=True, upload_to='images', verbose_name='Ссылка картинки страны'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='image',
            field=models.ImageField(blank=True, help_text='380x422px', null=True, upload_to='images', verbose_name='Ссылка картинки'),
        ),
    ]
