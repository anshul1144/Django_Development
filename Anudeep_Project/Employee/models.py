from django.db import models


class Employee(models.Model):
	employee_name = models.CharField(max_length=100)
	employee_email = models.EmailField(max_length=254)
	employee_salary = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.employee_name
