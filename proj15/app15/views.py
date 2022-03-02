from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'demo.html')

def wishes(request):
    return render(request,'test.html')

def message(request):
    return render(request,'sample.html')
