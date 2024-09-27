from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, name):
    return render(request, "hello/index.html", {
        "name": name.capitalize()
    })

def brian(request):
    return HttpResponse("Hello, Brian")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")