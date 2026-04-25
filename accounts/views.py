from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import StudentSignupForm, TeacherSignupForm


def signup_student(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student-dashboard')  # change to your route
    else:
        form = StudentSignupForm()
    return render(request, 'registration/signup_student.html', {'form': form})


def signup_teacher(request):
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher-dashboard')  # change to your route
    else:
        form = TeacherSignupForm()
    return render(request, 'registration/signup_teacher.html', {'form': form})


class RoleLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'role') and user.role == 'teacher':
            return reverse_lazy('teacher-dashboard')
        return reverse_lazy('student-dashboard')