from django.urls import path
from hello import views
from hello.models import LogMessage


home_list_view = views.HomeListView.as_view(
    context_object_name="message_list",
    template_name="hello/main.html",
)

urlpatterns = [
    path('', home_list_view, name='home'),
    path("main/", views.main, name="main"),
    path("country/<str:country_name>/", views.country, name="country"),
    
]