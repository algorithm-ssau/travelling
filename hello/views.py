import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage, Sight, Country
from django.views.generic import ListView


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
    image = country.imtitle
    context = {'image': image}
    print(country.imtitle)
    print(country.im1)
    # {{image1.user_image.url}}
    sights = Sight.objects.filter(country = Country.objects.get(nameCountry = country))
    for num, sight in enumerate(sights):
        print(f'{num}:{sight.image}')
        
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

