from django.shortcuts import render

# Create your views here.
def bheem(request):
    return render(request,'bheem.html')

def chutki(request):
    return render(request,'chutki.html')