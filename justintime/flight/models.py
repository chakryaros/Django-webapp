from django.db import models
from django.contrib.auth.models import User


class flight(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    from_city = models.CharField(max_length=30)
    to_city = models.CharField(max_length=30)
    flightName = models.CharField(max_length=80)
    type = models.CharField(max_length=30)
    seat = models.CharField(max_length = 100)
    price = models.PositiveSmallIntegerField(blank=True, default=None, null=True,)
    booker = models.ForeignKey(User, related_name='flight_booker', blank=True, null=True, on_delete=models.CASCADE,)
    destription = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.from_city+ ' ' + self.from_city + '_'+self.flightName+' '+self.type+' '+self.seat