from django.shortcuts import render
from .models import Student
# Create your views here.
def input(request):
    return render(request,'input.html')
def insertion(request):
    id=int(request.GET['id'])
    name=request.GET['name']
    add=request.GET['add']
    fee=float(request.GET['fee'])
    status=bool(request.GET['status'])
    s=Student(sid=id,sname=name,sadd=add,sfee=fee,sstatus=status)
    s.save()
    return render(request,'result.html')
def retrieve(request):
    data=Student.objects.all()
    return render(request,'display.html',{'records':data})
