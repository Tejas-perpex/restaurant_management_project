from django.db import models
from django.contrib.auth.models import User
from products.models import MenuItem


class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digit = 6 , decimal_place = 2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]

    customer = models.ForiegnKeyUser(User , on_delete = models.CASCADE)
    items = models.ManyToManyFields(MenuItem)
    total_amount = models.DecimalField(max_digit = 10 , decimal_place =2)
    status = models.CharField(max_length = 0 , choices = STATUS_CHOICES , default = 'PENDING')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"