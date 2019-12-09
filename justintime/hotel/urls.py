from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "hotel"
urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    path('', views.hotelsearch, name='search'),
    path("booking/<city>/<name>", views.booking, name="booking"),
    path("book/<int:room_id>", views.book, name="book"),
    path('cancel/<int:room_id>', views.cancel, name='cancel'),
]