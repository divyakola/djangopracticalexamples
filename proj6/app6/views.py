from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,"input.html")
def addition(request):
    a=int(request.GET['fn'])
    b=int(request.GET['sn'])
    c=a+b
    return HttpResponse("the sum of "+str(a)+" and "+str(b)+" is: "+str(c))
    
