from django.shortcuts import render, redirect

from .models import Student

# Create your views here.
def home(request):

    students = Student.objects.all()

    return render(request, "student/home.html", {'students':students})

def add_student(request):

    if request.method == 'POST':
        # to fetch and store the data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        attendance = request.POST.get('attendance')

        # to save all data in the database
        student = Student()
        student.student_name = name
        student.student_email = email
        student.student_attendance = attendance

        student.save()

        return redirect("/student/")

    return render(request, "student/add_student.html")
