from django.db import models
from django.contrib.auth.models import User

 

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


	
def __str__(self):
  return self.user.username

# class flight_status(models.Model):
#     flight = models.CharField(max_length=30)
#     from_place = models.CharField(max_length=30)
#     to_place = models.CharField(max_length=30)
#     depart_at_from = models.TimeField()
#     arrival_at_to = models.TimeField()
#     seat_no = models.IntegerField()
#     available = models.IntegerField()
#     collected = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.flight)+str(self.from_place)+str(self.to_place) + str(self.depart_at_from) + str(self.arrival_at_to)



# class reservation(models.Model):
#     # booked = models.ForeignKey(User)
#     no_of_seats = models.IntegerField()
#     # flight_status= models.ForeignKey(flight_status)
#     cost = models.IntegerField(default=0)
#     def __str__(self):
#         return str(self.flight_status)+str(self.booked)+str(self.no_of_seats)

class Hotel_detail:
    city : str
    name : str
    price : int
    image : str




