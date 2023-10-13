from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'user/login.html')
def udetails(request):
    return render(request,'user/udetails.html')
