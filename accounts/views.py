from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_not_required
from django.urls import reverse_lazy
from .forms import StudentSignupForm, InstructorSignupForm


@login_not_required
def signup_student(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # change to your route
    else:
        form = StudentSignupForm()
    return render(request, 'registration/signup_student.html', {'form': form})

@login_not_required
def signup_instructor(request):
    if request.method == 'POST':
        form = InstructorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # change to your route
    else:
        form = InstructorSignupForm()
    return render(request, 'registration/signup_instructor.html', {'form': form})


class RoleLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'role') and user.role == 'instructor':
            return reverse_lazy('dashboard')
        return reverse_lazy('dashboard')