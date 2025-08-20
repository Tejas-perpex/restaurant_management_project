from django.conf import settings
from django.shortcuts import render
from .models import RestaurantLocation

def homepage_view(request):
    location = RestaurantLocation.objects.first()
    restaurant_name = settings.RESTAURANT_NAME
    return render(request, 'homepage.html', {
        'location': location,
        'restaurant_name': restaurant_name
    })
