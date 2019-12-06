from django import forms
from users.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

class FlightForm(forms.Form):
    From = forms.CharField(max_length=100,label='From ',required=False)
    To = forms.CharField(max_length=100,label='Destination',required=False)
    no = forms.IntegerField(max_value=5,  min_value=1, label='Number of tickets',initial=1)