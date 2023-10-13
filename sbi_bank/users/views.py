from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def udetails(request):
    return render(request,'udetails.html')
