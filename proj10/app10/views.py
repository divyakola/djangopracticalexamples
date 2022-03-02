from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class ginput(View):
    def get(self,request):
        return render(request,"ginput.html")
class addition(View):
    def get(self,request):
        a=int(request.GET['fn'])
        b=int(request.GET['sn'])
        c=a+b
        return HttpResponse("the sum is:"+str(c))
