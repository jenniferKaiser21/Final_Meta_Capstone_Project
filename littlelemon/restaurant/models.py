from django.db import models


# Create your models here.


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.DecimalField(max_digits=6, decimal_places=0)
    BookingDate = models.DateTimeField()


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.DecimalField(max_digits=5, decimal_places=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'