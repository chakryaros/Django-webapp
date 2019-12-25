from django.shortcuts import render
from .models import flight
from django.contrib.auth.decorators import login_required
from .forms import FlightForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def flightsearch(request):
    if request.method == "POST":
        flight_search =FlightForm(request.POST)
        if flight_search.is_valid():
            cd = flight_search.cleaned_data
            if cd['from_city'] and cd['to_city']:
                db_flight = flight.objects.filter(from_city=cd['from_city'],to_city=cd['to_city'])
            else:
                db_flight=flight.objects.all()
            flight_form = FlightForm()
            return render(request,"flight/flight.html",{'db_flight': db_flight,'flight_form':flight_form})
    else:
        flight_form= FlightForm()
        return render(request, "flight/flight.html", {'flight_form':flight_form})


def booking(request, from_city, to_city):
    db_flight = flight.objects.filter(from_city=from_city, to_city=to_city)
 
    return render(request, "flight/booking.html", {'db':db_flight})

@login_required(login_url='/account/login/')
def book(request, flight_id):
    Flight = flight.objects.get( id=flight_id)

    if Flight.booker:
        return HttpResponse("Sorry, the room has already been booked")
    else:
        Flight.booker=request.user
        Flight.save()
        return HttpResponseRedirect('/flight/booking/'+Flight.from_city+'/'+Flight.to_city)


@login_required(login_url='/account/login/')
def cancel(request, flight_id):
    Flight = flight.objects.get( id=flight_id)
    if Flight.booker == request.user:
        Flight.booker=None
        Flight.save()
        return HttpResponseRedirect('/account/my-orders')