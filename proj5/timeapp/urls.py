from django.urls import path
from timeapp import views

urlpatterns=[
    path('cdt/',views.dateandtime)
    ]
