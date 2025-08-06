from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digit = 6 , decimal_place = 2)

    def __str__(self):
        return self.name

