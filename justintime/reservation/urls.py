from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('templates/',views.signin, name='signin'),
    path('flight/',views.flight, name='flight'),
    path('hotel/',views.hotel, name='hotel'),
    path('login/',LoginView.as_view(template_name="login.html"),name="hotel_login"),
    # path('logout/',LogoutView.as_view(),name="hotel_logout"),
    # path('templates/',views.RoomType,name="RoomType"),
    path('signup/',views.signup,name='signup'),
    
    ]