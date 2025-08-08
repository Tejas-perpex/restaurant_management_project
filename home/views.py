from django.shortcuts import render

def homepage_view(request):
    return render(request, 'home.html', {'restaurant_name': 'Tasty Bites'})




