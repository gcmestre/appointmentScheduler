from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from .models import Employee
# Create your views here.


class EmployeeList(ListView):
    model = Employee


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'


class EmployeeView(View):
    model = Employee
    fields = '__all__'
