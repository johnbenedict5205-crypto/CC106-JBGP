
from django.urls import path
from . import views

urlpatterns = [
    # Module 6
    path('', views.student_registration, name='student_registration'),
    path('success/', views.student_registration_success, name='student_registration_success'),

    # Module 7
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
