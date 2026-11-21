
from django.urls import path
from . import views

urlpatterns = [
    # ORIGINAL REGISTRATION URLS
    path('', views.student_registration, name='student_registration'),
    path('success/', views.registration_success, name='registration_success'),

    # STUDENT DIRECTORY
    path('students/', views.student_list, name='student_list'),

    # CREATE STUDENT
    path('students/create/', views.student_create, name='student_create'),

    # STUDENT DETAILS
    path('students/<int:pk>/', views.student_detail, name='student_detail'),

    # UPDATE STUDENT
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),

    # DELETE STUDENT
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
