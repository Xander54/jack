from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('location',views.location,name='location'),
    path('<str:num>/',views.mylocation,name='mylocation'),
    path('thanks',views.thanks,name='thanks')
]
