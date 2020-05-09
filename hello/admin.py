from django.contrib import admin
from .models import Sights
from .models import Country

admin.site.Register(Sights)
admin.site.Register(Country)

# Register your models here.
