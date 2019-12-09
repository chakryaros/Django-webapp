from django.shortcuts import render

# Create your views here.
def flightsearch(request):
    return render(request, "flight/flight.html")