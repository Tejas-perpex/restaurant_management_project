from django.conf import settings
from django.shortcuts import render

def homepage_view(request):
    phone_number = settings.RESTAURANT_PHONE
    return render(request, 'home.html', {'phone_number': phone_number})



