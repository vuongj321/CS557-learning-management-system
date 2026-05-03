from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_not_required
from accounts.forms import EditProfileForm

# Create your views here.
@login_not_required
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        if user.role == 'student' and hasattr(user, 'student_profile'):
            enrolled_courses = user.student_profile.course_set.all()
            context['enrolled_courses'] = enrolled_courses
            context['enrolled_count'] = enrolled_courses.count()
        elif user.role == 'instructor' and hasattr(user, 'instructor_profile'):
            teaching_courses = user.instructor_profile.course_set.all() if hasattr(user.instructor_profile, 'course_set') else []
            try:
                from courses.models import Course
                teaching_courses = Course.objects.filter(instructor=user.instructor_profile)
            except Exception:
                teaching_courses = []
            context['teaching_courses'] = teaching_courses
            context['teaching_count'] = len(teaching_courses)
            context['total_students'] = sum(course.students.count() for course in teaching_courses)

    return render(request, 'dashboard.html', context)

def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile/view.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'profile/edit.html', {'form': form, 'user': request.user})