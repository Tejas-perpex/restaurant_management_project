from django.shortcuts import render
from django.db import DatabaseError
from .models import MenuItem

def homepage(request):
    try:
        menu_items = MenuItem.objects.all()
    except DatabaseError as e:
        # Log the error if needed
        print(f"Database error: {e}")
        # Fallback to an empty list if DB query fails
        menu_items = []
        # You could also show an error message in the template
        error_message = "We are experiencing technical difficulties. Please try again later."
    else:
        error_message = None

    return render(request, "home.html", {
        "menu_items": menu_items,
        "error_message": error_message
    })



