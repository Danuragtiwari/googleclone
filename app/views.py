from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def go(request):
    if request.method=="POST":
        search=request.POST['go']
        url = 'https://www.ask.com/web?q='+search
    return render(request,'go.html')