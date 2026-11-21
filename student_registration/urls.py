
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', include('home.urls')),

    # STUDENT REGISTRATION
    path('registration/', include('registration.urls')),

    # STAFF LOGIN
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    # STAFF LOGOUT
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
