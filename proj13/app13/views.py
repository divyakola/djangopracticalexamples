from django.shortcuts import render

# Create your views here.
def welcome(request):
    message="hai siva krishna good morning"
    employes=[{'eid':101,'ename':'siva','sal':2000},
              {'eid':102,'ename':'rama','sal':3000},
              {'eid':103,'ename':'krishna','sal':4000}]
    return render(request,'output.html',{'msg':message,'emp':employes})
    
