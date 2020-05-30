import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage, Sight, Country
from django.views.generic import ListView
from django.views.generic.base import TemplateView


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

# class HomePageView(TemplateView):

#     template_name = "hello/main.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['countries'] = Country.objects.all()
#         context['sights'] = Sight.objects.all()[:3]
#         return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

#create method to render main page
def main(request):
    return render(request, "hello/main.html")

#create method to render country page
def country(request, country_name):
    country = Country.objects.get(nameCountry = "Австрия")
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
    sights = Sight.objects.filter(country = Country.objects.get(nameCountry = country_name))
    context = {'country': country,
               'images': image_list,
               'sights': sights
               }   
    return render(request, "hello/country.html", context)

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

