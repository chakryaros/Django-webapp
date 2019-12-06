# from django.urls import path
# from django.contrib.auth.views import LoginView,LogoutView
# from . import views

# dappx/urls.py
from django.conf.urls import url
from users import views
from django.views.generic import RedirectView
# SET THE NAMESPACE!
app_name = 'users'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^flight/$',views.flight,name='flight'),
    url(r'^hotel/$',views.hotel,name='hotel'),
    # url(r'^hotel_search/$',views.hotel_search,name='hotel_search'),
    # url(r'^result/$',views.result, name='result'),
    url(r'^hotel/$', RedirectView.as_view( permanent=False, url='users/hotel/result/'),name='result'),

]