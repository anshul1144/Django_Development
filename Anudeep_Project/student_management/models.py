from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.TextField(max_length=100)
    student_email = models.EmailField(max_length=254)
    student_attendance = models.IntegerField()
