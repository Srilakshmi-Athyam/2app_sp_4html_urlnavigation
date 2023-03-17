from django.shortcuts import render

# Create your views here.


def mickey(request):
    return render(request,'mickey.html')

def mouse(request):
    return render(request,'mouse.html')
