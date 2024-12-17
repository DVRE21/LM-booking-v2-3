from django.db import models
import datetime

# Create your models here.
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name

class Booking(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)
   first_name = models.CharField(max_length=200)
   reservation_date = models.DateField(default=datetime.date.today)
   reservation_slot = models.SmallIntegerField(default=10)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

 