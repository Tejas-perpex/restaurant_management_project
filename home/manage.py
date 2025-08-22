from myapp.models import Restaurant

restaurant = Restaurant.objects.create(
    name="The Great Indian Diner",
    address="123 Food Street, Mumbai",
    opening_hours={
        "Monday": "9 AM – 9 PM",
        "Tuesday": "9 AM – 9 PM",
        "Wednesday": "9 AM – 10 PM",
        "Thursday": "9 AM – 10 PM",
        "Friday": "9 AM – 11 PM",
        "Saturday": "10 AM – 11 PM",
        "Sunday": "Closed"
    }
)
