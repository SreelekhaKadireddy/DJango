from django.shortcuts import render
from userapp.models import Employee
# Create your views here.

def display_Employees(request):
    emp_list=Employee.objects.all()
    my_emp={'emp_list':emp_list}
    return render(request,'employee.html',context=my_emp)