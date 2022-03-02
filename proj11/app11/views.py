from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class ginput(View):
    def get(self,request):
        return render(request,'ginput.html')
class pinput(View):
    def get(self,request):
        return render(request,'pinput.html')

class addition(View):
    def get(self,request):
        a=int(request.GET['fn'])
        b=int(request.GET['sn'])
        c=a+b
        return render(request,'goutput.html',{'res':c})
    def post(self,request):
        a=int(request.POST['fn'])
        b=int(request.POST['sn'])
        c=a+b
        return render(request,'poutput.html',{'res':c})
        
