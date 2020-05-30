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
    descCountry=models.CharField(max_length=1000)
    currency=models.CharField(max_length=25,default='')
    language=models.CharField(max_length=150,default='')
    capital=models.CharField(max_length=20,default='')
    mapCountry=models.CharField(max_length=500,null =True)
    flag=models.ImageField(blank=True,upload_to='images',null=True,verbose_name='Флаг')
    imtitle=models.ImageField(blank=True, upload_to='images', null=True, help_text='380x250px', verbose_name='Ссылка картинки заголовка')
    im1=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 1')
    im2=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 2')
    im3=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 3')
    im4=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 4')
    im5=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 5')
    im6=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 6')
    im7=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 7')
    im8=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 8')
    im9=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 9')
    im0=models.ImageField(blank=True, upload_to='images/', null=True, help_text='380x250px', verbose_name='Ссылка картинки страны 10')
    def __str__(self):
        return f'{self.nameCountry}'

    def image_img(self):
            if self.im1:
                return u'<a href="{self.im.url}" target="_blank"><img src="{self.im.url}" width="100"/></a>'
            else:
                return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
                
class Sight(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название")
    price=models.CharField(max_length=20)
    address = models.CharField(max_length=55,default='')
    city=models.CharField(max_length=30,default='')
    timeOfWork=models.CharField(max_length=15,default='')
    description=models.CharField(max_length=1000)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    year_of_construction=models.CharField(max_length=15, null=True)
    image = models.ImageField(blank=True, upload_to='images', null=True, help_text='380x422px', verbose_name='Ссылка картинки')
    def __str__(self):
        return f'Название: {self.name}, страна:{self.country}'

    def image_img(self):
            if self.image:
                return u'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100"/></a>'
            else:
                return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
