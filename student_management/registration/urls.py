from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_registration, name='student_registration'),

    path(
        'register/success/',
        views.student_registration_success,
        name='student_registration_success'
    ),
]