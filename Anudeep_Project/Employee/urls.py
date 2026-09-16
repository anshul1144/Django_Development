from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("", views.home, name="home"),
    path("add-employee/", views.add_employee, name="add_employee"),
]
