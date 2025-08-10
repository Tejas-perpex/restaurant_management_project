from django.shortcuts import render
from datetime import datetime

def homepage(request):
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'home.html', context)


