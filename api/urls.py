from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.welcome, name="welcome"),
    path('', views.Signup, name="signup"),
    path('home', views.LandingPage, name='landingpage'),
    path('reviews', views.Review, name='reviews'),
    path('weather',views.Weather, name='WeatherData'),
    path('login', views.login, name="login"),
    path('contactus', views.contact, name="contactus"),
    path('myprofile', views.MyProfile, name="myprofile"),
]