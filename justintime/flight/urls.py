from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "flight"
urlpatterns = [

    path('', views.flightsearch, name='search'),
    path("booking/<from_city>/<to_city>", views.booking, name="booking"),
    path("book/<int:flight_id>", views.book, name="book"),
    path('cancel/<int:flight_id>', views.cancel, name='cancel'),
]