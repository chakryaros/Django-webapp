from django.shortcuts import render


from users.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Hotel_detail

def index(request):
    return render(request,'users/index.html')

def flight(request):
   
    return render(request,'users/flight.html')

# def result(request):
   
#     return render(request,'users/result.html')

def hotel(request):

    hotel1 =  Hotel_detail()
    hotel1.city = "Denver"
    hotel1.name = "Hilton Hotel"
    hotel1.price = "100"
    hotel1.image = "hotel.jpg"

    hotel2 =  Hotel_detail()
    hotel2.city = "Boulder"
    hotel2.name = "Liberty"
    hotel2.price = "150"
    hotel2.image = "Hilton.jpg"

    list_hotel = [hotel1, hotel2]
   
    return render(request,'users/hotel.html', {'list_hotel ' : list_hotel})

def contact(request):
   
    return render(request,'users/contact.html')
    
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'users/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'users/login.html', {})

def result(request):

    if request.POST =="where_to_stay" and request.POST =="hotel_name":

        hotel1 =  Hotel_detail()
        hotel1.city = "Denver"
        hotel1.name = "Hilton Hotel"
        hotel1.price = "100"
        hotel1.image = "hotel.jpg"

        hotel2 =  Hotel_detail()
        hotel2.city = "Boulder"
        hotel2.name = "Liberty"
        hotel2.price = "150"
        hotel2.image = "Hilton.jpg"

        list_hotel = [hotel1, hotel2]
        return redirect(request,"users/result", {'list_hotel ' : list_hotel})


# def hotel_search(request):
#     staycity = request.POST["where_to_stay"]
#     hotelname = request.POST["hotel_name"]
#     staycity = "Denver"
#     hotelname = ["Hilton Hotel", "Liberty International Airport Hotel", "Holiday Inn", "Liberty International Airport Hotel"]

#     return render(request, 'result.html', {'result' : hotelname})
