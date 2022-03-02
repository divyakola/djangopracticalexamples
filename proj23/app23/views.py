from django.shortcuts import render
from .forms import EmployeForm
from .models import EmployeModel
from django.http import HttpResponse
# Create your views here.
def input(request):
    emp_form=EmployeForm()
    return render(request,'input.html',{'emp':emp_form})
    
def insert(request):
    emp_form=EmployeForm(request.POST)
    if emp_form.is_valid():
        emp_form.save()
        return HttpResponse("Inserted Successfully")

def retrive(request):
    data=EmployeModel.objects.all()
    return render(request,'display.html',{'records':data})
