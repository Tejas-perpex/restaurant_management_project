from django.shortcuts import render
from django.conf import settings

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
    return render(request, "home.html", {"restaurant_name": restaurant_name})

def about(request):
    return render(request, "about.html")

