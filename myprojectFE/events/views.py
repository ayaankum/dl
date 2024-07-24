from django.shortcuts import render
from .models import Fruit, Student
def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request, 'events/fruits.html', {'fruits': fruits})
def student_list(request):
    students = Student.objects.filter(selected=True)
    return render(request, 'events/Student.html', {'students': students})