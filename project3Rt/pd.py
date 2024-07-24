# populate_database.py

import os
import django

# Set up Django environment (modify 'myproject' to your actual project name)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project3.settings')
django.setup()

from registration.models import Course, Student  # Import your models

def populate_data():
    # Create Course instances
    course1 = Course(name='Mathematics', description='An introductory course to Mathematics.')
    course1.save()

    course2 = Course(name='Physics', description='An introductory course to Physics.')
    course2.save()

    
    student1 = Student(name='Alice Smith', email='alice@example.com')
    student1.save()
    student1.courses.add(course1, course2)  # Assign courses

    student2 = Student(name='Bob Johnson', email='bob@example.com')
    student2.save()
    student2.courses.add(course1)  # Assign courses

    # Display the inserted data
    print("Courses added:")
    for course in Course.objects.all():
        print(f"- {course.name}: {course.description}")

    print("\nStudents added:")
    for student in Student.objects.all():
        courses = ', '.join([course.name for course in student.courses.all()])
        print(f"- {student.name}: {student.email}, Courses: {courses}")

if __name__ == '__main__':
    populate_data()
