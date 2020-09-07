from django.contrib import admin
from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path("", EmployeeList.as_view())
]
