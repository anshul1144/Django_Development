from django.db import models
# Create your models here.

class Student(models.Model):
    student_name = models.TextField(max_length=100)
    student_email = models.EmailField()
    student_age = models.IntegerField()
    student_attendance = models.IntegerField(default=False)

    def __str__(self):
        return self.student_name