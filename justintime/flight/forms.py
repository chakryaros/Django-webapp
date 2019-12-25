from django import forms

from django.contrib.auth.models import User
from .models import *




class FlightForm(forms.Form):
    from_city = forms.CharField(required=False)
    to_city = forms.CharField(required=False)
    # To = forms.CharField(max_length=100,label='Destination',required=False)
    # no = forms.IntegerField(max_value=5,  min_value=1, label='Number of tickets',initial=1)


