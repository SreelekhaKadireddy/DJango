from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login),
    path('udetails/', views.udetails),
]