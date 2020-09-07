"""appointmentScheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, reverse
from appointment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'), name="account"),
    path('employee/', EmployeeList.as_view(), name="employee-list"),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name="employee-detail"),
    path('employee/<int:pk>/edit', EmployeeUpdate.as_view(), name="employee-update"),
    path('employee/create/', EmployeeCreate.as_view(), name="employee-create"),
    path('client/', ClientList.as_view(), name="client-list"),
    path('client/<int:pk>/', ClientDetail.as_view(), name="client-detail"),
    path('client/<int:pk>/edit', ClientUpdate.as_view(), name="client-update"),
    path('client/create/', ClientCreate.as_view(), name="client-create"),
    path('appointment/', AppointmentList.as_view(), name="appointment-list"),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name="appointment-detail"),
    path('appointment/<int:pk>/edit', AppointmentUpdate.as_view(), name="appointment-update"),
    path('appointment/create/', AppointmentCreate.as_view(), name="appointment-create"),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
]
