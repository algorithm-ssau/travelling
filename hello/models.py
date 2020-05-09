from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Country(models.Model):
    nameCountry=models.CharField(max_length=20)
    descCountry=models.CharField(max_length=50)
    im=models.ImageField(blank=True, upload_to='images', null=True, help_text='150x150px', verbose_name='Ссылка картинки страны')
    def __str__(self):
        return f'Название: {self.nameCountry}, описание:{self.descCountry}'

    def image_img(self):
            if self.im:
                return u'<a href="{self.im.url}" target="_blank"><img src="{self.im.url}" width="100"/></a>'
            else:
                return '(Нет изображения)'

                
class Sights(models.Model):
   
    name=models.CharField(max_length=50, verbose_name="Название")
    price=models.IntegerField()
    description=models.CharField(max_length=200)

    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    year_of_construction=models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images', null=True, help_text='150x150px', verbose_name='Ссылка картинки')


    def __str__(self):
        return f'Название: {self.name}, год постройки: {self.year_of_construction}, цена на вход: {self.price}, страна:{self.country}'

    def image_img(self):
            if self.image:
                return u'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100"/></a>'
            else:
                return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
