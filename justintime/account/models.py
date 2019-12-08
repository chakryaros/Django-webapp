from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100, blank=True)
    birth = models.DateField(blank = True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(blank=True)


    def __str__(self):
        return "user:{}".format(self.user.username)
