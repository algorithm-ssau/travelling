# Generated by Django 3.0.4 on 2020-05-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20200514_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='imtitle',
            field=models.ImageField(blank=True, help_text='380x250px', null=True, upload_to='images', verbose_name='Ссылка картинки заголовка'),
        ),
        migrations.AlterField(
            model_name='country',
            name='mapCountry',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
