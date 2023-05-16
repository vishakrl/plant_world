from django.shortcuts import render
from django.http import HttpRequest

# Create your views .
def index(request):
    return render(request,"index.html") 

def click(request):
    return render(request,"text.html",{'val':'java'})
