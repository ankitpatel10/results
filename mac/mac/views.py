from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("Hello")

def index(request):
    return render(request, 'mac/html/index.html')
