from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Reviews, WeatherData, Address, ContactUs
import requests
import json
import numpy as np
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# global_name = ""
# global_mail = ""



def Signup(request):
    
    return render(request, "api/signup.html")

def LandingPage(request):
      authname = request.POST.get('AuthName')
      authmail = request.POST.get('AuthMail')
      authpass = request.POST.get('AuthPassword')
      auth_user = authenticate( username=authname, email=authmail, password=authpass)
       
      name = request.POST.get('full_name')
      review = request.POST.get('review')
      new_review = Reviews.objects.create(username=name, body=review)
      new_review.save()
      
      contactname = request.POST.get('contactname')
      contactemail = request.POST.get('contactemail')
      contactmsg = request.POST.get('message')
      
      new_contact = ContactUs(username=contactname, email=contactemail, message=contactmsg)
      new_contact.save()
      
      # if auth_user is None:
        #  return render(request,"api/login.html")

      # return render(request,"api/login.html")
 
      
      return render(request,"api/home.html") 

def login(request):
      name = str(request.POST.get('Username'))
      mail = request.POST.get('Email')
      Password = request.POST.get('Password')
      print(name)
      print(mail)
      user = User.objects.create_user(username=name, email=mail, password=Password)
      user.save()
  
      return render(request, "api/login.html")
    

def Review(request):
   return render(request, 'api/reviews.html')

def Weather(request):
  r = request.POST
  print(r)
   
  
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2696dd3de015ae6c54e56ae12c77b507'
  cities = ['Patiala']
  TempSum=0
  WeatherStatus=[]
  for city in cities:
    Response = requests.get(url.format(city))
    data = eval(Response.text)
    
    print(data)
    
    WeatherStatus.append({str(city) : [str(data['weather'][0]['description']), str(data['main']['humidity']), str(data['wind']['speed'])]})
    TempSum = data['main']['temp']
    # AvgTemp = TempSum/len(cities)
    DictData = {"Weather":WeatherStatus, "Average temperature":TempSum}
    print(DictData)
    FullData = WeatherData.objects.create(JourneyWeather = json.dumps(DictData))
    FullData.save()
    
    return render(request, 'api/weather.html', context={'weather':[str(city),str(data['weather'][0]['description']),str(data['main']['humidity']), str(data['wind']['speed']), TempSum]})





def contact(request):
  return render(request, 'api/contactus.html')

def MyProfile(request):
  
  return render(request, 'api/myprofile.html')