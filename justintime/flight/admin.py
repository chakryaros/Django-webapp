from django.contrib import admin
from flight.models import flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ('from_city', 'to_city', 'flightName', 'type', 'seat')
    list_filter = ('flightName','seat',)

admin.site.register(flight, FlightAdmin)