from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=30)
    beds = models.CharField(max_length = 100)
    price = models.PositiveSmallIntegerField(blank=True, default=None, null=True,)
    booker = models.ForeignKey(User, related_name='room_booker', blank=True, null=True, on_delete=models.CASCADE,)
    destription = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.city+'_'+self.name+' '+self.type+' '+self.beds