import phonenumbers
import opencage
import folium
from django.shortcuts import render,redirect
from .models import Phonebook,User
from phonenumbers import geocoder,carrier
from opencage.geocoder import OpenCageGeocode
import os
from django.http import HttpResponse
import random


# Create your views here.


def index(request):
    return render(request,'location/index.html')
def location(request):
   
    
  
        if request.method=='POST':
            phone_number=request.POST['phone']
            
            pepnumber=phonenumbers.parse(phone_number)
            location=geocoder.description_for_number(pepnumber,"en")
            service_pro=carrier.name_for_number(pepnumber,'en')
            key="4f4c8aa5b22b486393f8a75b7eec5752"
            geocod=OpenCageGeocode(key)
            query=str(location)
            result=geocod.geocode(query)
            lat=result[0]['geometry']['lat']
            lng=result[0]['geometry']['lng']
            myMap=folium.Map(location=[lat,lng],zoom_start=9)
            folium.Marker([lat,lng],popup=location).add_to(myMap)
            crypto=random.randrange(0,int(phone_number[0:]))
            der=os.getcwd()
            os.chdir('/var/task/location_holder/templates/location')
            
            myMap.save('mylocation'+str(crypto)+'.html',False)
           
                
            return render(request,'location/wait.html',{'phone':phone_number,'key':str(crypto),'network':der,'location':location})
            
        else:
            redirect('index')
        
def mylocation(request,num):
   
    return render(request,'location/'+'mylocation'+num+'.html')
def thanks(request):
    comment=request.POST['text']
    email=request.POST['email']
    inf=User(email=email,comment=comment)
    inf.save()
    return redirect('index')
    
