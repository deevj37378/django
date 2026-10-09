from django.db import models

# Create your models here.
class MenuItem(models.Model): #This class will create a table in the database with these rows
    name = models.CharField(max_length=255) #This will be a row in a database
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)