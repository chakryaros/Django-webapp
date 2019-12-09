from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
from .forms import RoomSearchForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def hotelsearch(request):
    if request.method == "POST":
        hotel_search =RoomSearchForm(request.POST)
        if hotel_search.is_valid():
            cd = hotel_search.cleaned_data
            if cd['city'] and cd['name']:
                db=Room.objects.filter(city=cd['city'],name=cd['name'])
            elif cd['city']:
                db = Room.objects.filter(city=cd['city'])
            elif cd['name']:
                db = Room.objects.filter(name=cd['name'])
            else:
                db=Room.objects.all()
            hotel_form = RoomSearchForm()
            return render(request,"hotel/hotel.html",{'db':db,'hotel_form':hotel_form})
    else:
        hotel_form= RoomSearchForm()
        return render(request, "hotel/hotel.html", {'hotel_form':hotel_form})

def booking(request, city, name):
    db = Room.objects.filter(city=city, name=name)
 
    return render(request, "hotel/booking.html", {'db':db})

@login_required(login_url='/account/login/')
def book(request, room_id):
    room = Room.objects.get( id=room_id)

    if room.booker:
        return HttpResponse("Sorry, the room has already been booked")
    else:
        room.booker=request.user
        room.save()
        return HttpResponseRedirect('/hotel/booking/'+room.city+'/'+room.name)


@login_required(login_url='/account/login/')
def cancel(request, room_id):
    room = Room.objects.get( id=room_id)
    if room.booker == request.user:
        room.booker=None
        room.save()
        return HttpResponseRedirect('/account/my-orders')