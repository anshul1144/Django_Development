from django.test import TestCase

from .models import Employee


class EmployeeViewsTests(TestCase):
	def test_employee_pages_render(self):
		self.assertEqual(self.client.get("/employee/").status_code, 200)
		self.assertEqual(
			self.client.get("/employee/add-employee/").status_code,
			200,
		)

	def test_add_employee_creates_employee(self):
		response = self.client.post(
			"/employee/add-employee/",
			{
				"name": "Ada Lovelace",
				"email": "ada@example.com",
				"salary": "85000.00",
			},
		)

		self.assertRedirects(response, "/employee/")
		self.assertEqual(Employee.objects.count(), 1)
		self.assertEqual(Employee.objects.get().employee_name, "Ada Lovelace")
