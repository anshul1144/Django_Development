from django.shortcuts import redirect, render

from .models import Employee


def home(request):
	employees = Employee.objects.all()
	return render(request, "Employee/home.html", {"employees": employees})


def add_employee(request):
	if request.method == "POST":
		Employee.objects.create(
			employee_name=request.POST.get("name", "").strip(),
			employee_email=request.POST.get("email", "").strip(),
			employee_salary=request.POST.get("salary", "").strip(),
		)
		return redirect("employee:home")

	return render(request, "Employee/add_employee.html")
