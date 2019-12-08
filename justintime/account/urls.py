from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('contact/', views.contact, name='contact'),
    path('my-information/', views.myself, name='my_information'),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    path('my-image/', views.my_image, name='my_image'),
    path('my-orders/', views.my_orders, name='my_orders')

]