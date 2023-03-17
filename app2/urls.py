from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns=[
    path('mouse/',mouse,name='mouse'),
    path('mickey/',mickey,name='mickey'),
]