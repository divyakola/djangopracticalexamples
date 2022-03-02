from django.shortcuts import render
from .forms import customer
# Create your views here.
def cust_info(request):
    c_obj=customer()
    return render(request,"cust.html",{'c':c_obj})
