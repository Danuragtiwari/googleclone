from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def go(request):
    return render(request,'go.html')