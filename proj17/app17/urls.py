from django.urls import path,re_path
from app17 import views

urlpatterns=[
    path('in/',views.input),
    re_path('insert',views.insertion),
    re_path('display',views.retrieve)
    ]
