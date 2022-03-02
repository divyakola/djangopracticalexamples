#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def morning(request):
    return HttpResponse("Hello Siva! Good Morning")

def afternoon(request):
    return HttpResponse("Hello Siva! Good Afternoon")

def evening(request):
    return HttpResponse("Hello Siva! Good Evening")

def night(request):
    return HttpResponse("Hello Siva! Good Night")

