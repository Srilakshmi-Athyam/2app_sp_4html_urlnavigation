from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('bheem/',bheem,name='bheem'),
    path('chutki/',chutki,name='chutki'),
]