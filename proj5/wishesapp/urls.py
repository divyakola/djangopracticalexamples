from django.urls import path
from wishesapp import views

urlpatterns=[
    path('mg/',views.morning),
    path('af/',views.afternoon),
    path('eve/',views.evening),
    path('nt/',views.night)
    ]
