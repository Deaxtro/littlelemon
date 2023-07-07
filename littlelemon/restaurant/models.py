from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])
    BookingDate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title}: {self.price}"