import json

from django.shortcuts import render
from .models import Connection, Feedback,Passangers
from .forms import feedbackForm, flightsearchform
# Create your views here.


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def connection(request):
    connection = Connection.objects.all
    return render(request ,'connection.html',{'connection':connection})

def feedback(request):
    feedback = Feedback.objects.all
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            p = form.save()
            p.save()

    else:
        form = feedbackForm()
    return render(request,"feed.html",{"feedback":feedback,"form":form})


def passangers(request):
    passanger = Passangers.objects.all
    return render(request,'passanger.html',{"passanger":passanger})


def flight_search(request):
    flights = Connection.objects.order_by('place_of_origin')
    origins = set()
    destinitions = {}
    for flight in flights:
        origins.add(flight.place_of_origin)
        if not flight.place_of_origin in destinitions:
            destinitions[flight.place_of_origin]= set()
        destinitions[flight.place_of_origin].add(flight.place_of_destination)
    for key in destinitions:
        destinitions[key]=list(destinitions[key])
    flightsearch = flightsearchform()
    return render(request,'flightsearch.html',{'origins':'origins','destinitions':json.dumps(destinitions),'flights':'flights','form':flightsearch})

