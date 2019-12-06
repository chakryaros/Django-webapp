from django.shortcuts import render
# ,render_to_response,redirect
from django.http import HttpResponse
# from Reserve.models import Roomtype
# from django.template import context, loader
# from django.contrib.auth import (authenticate,get_user_model,login,logout)
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def index(request):

    return render(request,'index.html')

def login(request):
    #rooms = Roomtype.objects.all()
    return render(request,'login.html')

def flight(request):
    #rooms = Roomtype.objects.all()
    return render(request,'flight.html')

def hotel(request):
    #rooms = Roomtype.objects.all()
    return render(request,'hotel.html')

def contact(request):
    #rooms = Roomtype.objects.all()
    return render(request,'contact.html')

# def RoomType(request):
#     rooms = Roomtype.objects.all()
#     return render(request,'RoomType.html',{'rooms':rooms})

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=user,set_password=password)
            form.save()
            login(request,user)
        return redirect(request,'login.html')
    else:
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})

def home(request):

    return render(request,'home.html')


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, 'result.html', {'result' : res})




