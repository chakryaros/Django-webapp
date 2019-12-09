from django import forms
from django.contrib.auth.models import User
from .models import Room
class RoomSearchForm(forms.Form):
    city = forms.CharField(required=False)
    name = forms.CharField(required=False)
