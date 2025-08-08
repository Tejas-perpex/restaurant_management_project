from django.shortcuts import render

def menu_list(request):
    # Hardcoded menu items for now
    menu_items = [
        {"name": "Margherita Pizza", "price": 8.99},
        {"name": "Pasta Alfredo", "price": 10.50},
        {"name": "Caesar Salad", "price": 6.75},
    ]
    return render(request, "menu.html", {"menu_items": menu_items})


