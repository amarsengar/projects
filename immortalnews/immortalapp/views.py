from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'immortalapp/index.html')


def hydjobs(request):
    jobs_list = Hyd_jobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'immortalapp/hydjobs.html',context=my_dict)

def blrjobs(request):
    return render(request,'immortalapp/blrjobs.html')

def chennaijobs(request):
    return render(request,'immortalapp/chennaijobs.html')

def punejobs(request):
    return render(request,'immortalapp/punejobs.html')
