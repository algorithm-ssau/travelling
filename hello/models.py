from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class User(models.Model):
    login=models.CharField(max_length=50, verbose_name="Логин")
    password=models.CharField(max_length=30, verbose_name="Пароль")
    
class Sights(models.Model):
    COUNTRY_CHOICES ={
        (Russia, "Russia"),
        (Italy, "Italy"),
        (France, "France"),
        (Germany, "Germany"),
        (Norway, "Norway"),
    }
    name=models.CharField(max_length=50, verbose_name="Название")
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    country=models.CharField(choises=COUNTRY_CHOICES)
    year_of_construction=models.IntegerField()