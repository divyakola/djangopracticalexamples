from django.shortcuts import render
from datetime import datetime
# Create your views here.
def welcome(request):
    employes=[{'eid':101,'ename':'siva','sal':2000},
              {'eid':102,'ename':'rama','sal':4000},
              {'eid':103,'ename':'krishna','sal':3000}
              ]
    cdt=datetime.now()
    context={'emp':employes,'now':cdt}
    return render(request,'display.html',context)
              
