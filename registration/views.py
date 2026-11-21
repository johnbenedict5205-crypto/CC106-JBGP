
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Student
from .forms import StudentForm


# CHECK IF USER IS AN AUTHORIZED STAFF MEMBER
def staff_check(user):
    return user.is_authenticated and user.is_staff


# STAFF DASHBOARD - MODULE 09 ENHANCED
@user_passes_test(staff_check, login_url='login')
def staff_dashboard(request):

    # 1. Count all Student records
    total_students = Student.objects.count()

    # 2. Count Male and Female students
    male_students = Student.objects.filter(
        Q(gender__iexact='M') |
        Q(gender__iexact='Male')
    ).count()

    female_students = Student.objects.filter(
        Q(gender__iexact='F') |
        Q(gender__iexact='Female')
    ).count()

    # 3. Calculate percentages safely
    male_percent = (
        male_students / total_students * 100
        if total_students > 0 else 0
    )

    female_percent = (
        female_students / total_students * 100
        if total_students > 0 else 0
    )

    # 4. Read search term from URL
    query = request.GET.get('q', '').strip()

    # 5. Prepare student report
    students = Student.objects.all().order_by(
        'last_name',
        'first_name'
    )

    # 6. Filter report when search term is supplied
    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    # 7. Send values to dashboard template
    context = {
        'total_students': total_students,
        'male_students': male_students,
        'female_students': female_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'students': students,
        'query': query,
    }

    return render(
        request,
        'registration/dashboard.html',
        context
    )


# ORIGINAL STUDENT REGISTRATION - PUBLIC ACCESS
def student_registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        contact_no = request.POST.get('contact_no')

        Student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            contact_no=contact_no
        )

        return redirect('registration_success')

    return render(request, 'registration/registration.html')


# REGISTRATION SUCCESS PAGE - PUBLIC ACCESS
def registration_success(request):
    return render(request, 'registration/success.html')


# STUDENT DIRECTORY AND SEARCH - STAFF ONLY
@user_passes_test(staff_check, login_url='login')
def student_list(request):
    query = request.GET.get('q', '').strip()

    students = Student.objects.all().order_by(
        'last_name',
        'first_name'
    )

    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        'students': students,
        'query': query,
    }

    return render(
        request,
        'registration/student_list.html',
        context
    )


# STUDENT DETAIL PAGE - STAFF ONLY
@user_passes_test(staff_check, login_url='login')
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        'registration/student_detail.html',
        {'student': student}
    )


# CREATE NEW STUDENT - STAFF ONLY
@user_passes_test(staff_check, login_url='login')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student record created successfully.'
            )
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'page_title': 'Register Student'
        }
    )


# UPDATE EXISTING STUDENT - STAFF ONLY
@user_passes_test(staff_check, login_url='login')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student record updated successfully.'
            )
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'page_title': 'Update Student',
            'student': student
        }
    )


# DELETE STUDENT - STAFF ONLY
@user_passes_test(staff_check, login_url='login')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(
            request,
            'Student record deleted successfully.'
        )
        return redirect('student_list')

    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student}
    )
