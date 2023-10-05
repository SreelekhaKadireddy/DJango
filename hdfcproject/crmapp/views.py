from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Home page<h1>')
def about(request):
    return HttpResponse('<h1>About page<h1>')
def services(request):
    return HttpResponse('<h1>Services page<h1>')
def contact(request):
    return HttpResponse('<h1>Contact page<h1>')

