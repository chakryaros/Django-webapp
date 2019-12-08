from django.contrib import admin


# Register your models here.
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('city', 'name', 'type', 'beds')
    list_filter = ('city','name',)

admin.site.register(Room, RoomAdmin)