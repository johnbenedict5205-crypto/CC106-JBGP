from django.shortcuts import render, redirect
from .models import Student


def student_registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender_name = request.POST.get('gender_name')
        date_of_birth = request.POST.get('date_of_birth')
        contact_number = request.POST.get('contact_number')

        # Save student information to the database
        Student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            gender_name=gender_name,
            date_of_birth=date_of_birth,
            contact_number=contact_number
        )

        # Redirect to success page
        return redirect('student_registration_success')

    # Display registration form
    return render(request, 'registration/student_registration.html')


def student_registration_success(request):
    return render(request, 'registration/success.html')