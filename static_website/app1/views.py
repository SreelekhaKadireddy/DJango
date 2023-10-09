from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hello, welcome to index page</h1>')

def about(request):
    return render(request,'about.html')