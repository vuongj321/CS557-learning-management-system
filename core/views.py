from django.shortcuts import render
from django.contrib.auth.decorators import login_not_required

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
        # Handle profile update logic here (e.g., form validation, saving changes)
        pass
    user = request.user
    context = {'user': user}
    return render(request, 'profile/edit.html', context)