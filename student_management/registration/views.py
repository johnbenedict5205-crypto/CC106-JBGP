
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm


# EXISTING MODULE 6: Student Registration
def student_registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender_name = request.POST.get('gender_name')
        date_of_birth = request.POST.get('date_of_birth')
        contact_number = request.POST.get('contact_number')

        Student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            gender_name=gender_name,
            date_of_birth=date_of_birth,
            contact_number=contact_number
        )

        return redirect('student_registration_success')

    return render(request, 'registration/student_registration.html')


def student_registration_success(request):
    return render(request, 'registration/success.html')


# MODULE 7: Student Directory and Search
def student_list(request):
    query = request.GET.get('q', '')

    students = Student.objects.all().order_by('last_name')

    if query:
        students = students.filter(
            student_id__icontains=query
        ) | students.filter(
            first_name__icontains=query
        ) | students.filter(
            last_name__icontains=query
        )

    return render(request, 'registration/student_list.html', {
        'students': students,
        'query': query,
    })


# MODULE 7: Student Details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(request, 'registration/student_detail.html', {
        'student': student,
    })


# MODULE 7: Add Student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'registration/student_form.html', {
        'form': form,
        'title': 'Add New Student',
    })


# MODULE 7: Update Student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'registration/student_form.html', {
        'form': form,
        'title': 'Update Student',
    })


# MODULE 7: Delete Student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

    return render(request, 'registration/student_confirm_delete.html', {
        'student': student,
    })
