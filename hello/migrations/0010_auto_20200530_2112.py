# Generated by Django 3.0.4 on 2020-05-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20200530_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='price',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='sight',
            name='timeOfWork',
            field=models.CharField(default='', max_length=25),
        ),
    ]
