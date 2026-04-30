from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/student/', views.signup_student, name='signup_student'),
    path('signup/instructor/', views.signup_instructor, name='signup_instructor'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]