#from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def dateandtime(request):
    now=datetime.now()
    return HttpResponse("The current system date and time is:"+str(now))
