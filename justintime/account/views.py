from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from hotel.models import Room

# Create your views here.

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                
                return HttpResponse("Invalid login details given")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})





def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/registed.html')
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()

        return render(request, "account/registration.html", {"user_form": user_form})


def contact(request):
    return render(request, 'account/contact.html')


@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userprofile = UserProfile.objects.get(user=request.user.id)
        userprofile.photo = img
        userprofile.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)

@login_required(login_url='/account/login/')
def myself(request):

    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    return render(request, "account/myself.html", {"user":request.user, "userprofile":userprofile})

@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userprofile.email = userprofile_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']

            userprofile.address = userprofile_cd['address']
            request.user.save()
            userprofile.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth":userprofile.birth, "phone":userprofile.phone,"address":userprofile.address})
        return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form})

@login_required(login_url='/account/login/')
def my_orders(request):
    room_db=Room.objects.filter(booker=request.user)
    return render(request, "account/my_orders.html", {"room_db":room_db})
