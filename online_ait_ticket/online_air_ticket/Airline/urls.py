from django.urls import path

from . import views

app_name = 'Airline'





urlpatterns = [
    path('', views.index),
    path('home/',views.home,name='home'),
    path('about',views.About,name='about'),
    path('con/',views.connection),
    path('feed/',views.feedback, name='feed'),
    path('passanger/',views.passangers, name ='passanger'),
    path('flight/',views.flight_search, name='flight')



]