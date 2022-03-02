from django.shortcuts import render
from .forms import empForm
from django.http import HttpResponse
from .models import emp
# Create your views here.
def input(request):
    ef=empForm()
    return render(request,'input.html',{'eform':ef})
def insertion(request):
    ef=empForm(request.POST)
    if ef.is_valid():
        ef.save()
        return HttpResponse("Inserted Successfully")
def retreive(request):
    data=emp.objects.all()
    return render(request,'display.html',{'records':data})
    
        
    
