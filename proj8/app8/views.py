from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ginput(request):
    return render(request,'ginput.html')
def pinput(request):
    return render(request,'pinput.html')

def addition(request):
    if request.method=="GET":
        a=int(request.GET['fn'])
        b=int(request.GET['sn'])
        c=a+b
        return HttpResponse("the sum of "+str(a)+" and "+str(b)+" is: "+str(c))
    elif request.method=="POST":
        a=int(request.POST['fn'])
        b=int(request.POST['sn'])
        c=a+b
        return HttpResponse("the sum of "+str(a)+" and "+str(b)+" is: "+str(c))
