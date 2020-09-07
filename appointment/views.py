from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from .models import Employee, Client, Appointment
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


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    fields = '__all__'


class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'


class AppointmentList(ListView):
    model = Appointment


class AppointmentDetail(DetailView):
    model = Appointment


class AppointmentCreate(CreateView):
    model = Appointment
    fields = '__all__'


class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = '__all__'

