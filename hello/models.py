from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


    
class Sights(models.Model):
    COUNTRY_CHOICES ={
        ("RUSSIA", "Russia"),
        ("ITALY", "Italy"),
        ("FRANCE", "France"),
        ("GERMANY", "Germany"),
        ("NORWAY", "Norway"),
    }
    name=models.CharField(max_length=50, verbose_name="Название")
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    country=models.CharField(choices=COUNTRY_CHOICES)
    year_of_construction=models.IntegerField()

    def __str__(self):
        return 'Название: {0}, год постройки: {1}, цена на вход: {2}, страна:'.format(self.name,self.year_of_construction,self.price)