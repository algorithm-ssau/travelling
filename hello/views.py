import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage, Sight, Country
from django.views.generic import ListView
from django.views.generic.base import TemplateView


    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
        
#create method to render main page
def main(request):
    return render(request, "hello/main.html")

#create method to render country page
def country(request, country_name):
    country = Country.objects.get(nameCountry = country_name)
    image_list = [country.im1,
                  country.im2, 
                  country.im3,
                  country.im4,
                  country.im5,
                  country.im6,
                  country.im7,
                  country.im8,
                  country.im9,
                  country.im0]
    sights = Sight.objects.filter(country = country)
    context = {'country': country,
               'images': image_list,
               'sights': sights
               }   
    return render(request, "hello/country.html", context)



