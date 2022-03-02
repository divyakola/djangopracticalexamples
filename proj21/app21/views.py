from django.shortcuts import render
from .forms import student_form
# Create your views here.
def info(request):
    std_obj=student_form()
    return render(request,'input.html',{'std':std_obj})
