from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('signup/student/', views.signup_student, name='signup-student'),
    path('signup/instructor/', views.signup_instructor, name='signup-instructor'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]