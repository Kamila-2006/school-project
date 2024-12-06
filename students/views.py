from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from teachers.models import Teacher
from groups.models import Group


def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    return render(request, 'index.html', {'students': students, 'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if first_name and last_name and age and email:
            Student.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                email = email
            )
            return redirect('students:list')
    return render(request, 'students/student-form.html')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student':student}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')