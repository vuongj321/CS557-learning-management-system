from django.shortcuts import render, redirect, get_object_or_404

from .models import Assignment
from .forms import AssignmentForm
from courses.models import Course


def assignment_list(request):

    if request.user.role == 'student':
        student_profile = request.user.student_profile
        courses = Course.objects.filter(students=student_profile)

    elif request.user.role == 'instructor':
        instructor_profile = request.user.instructor_profile
        courses = Course.objects.filter(instructor=instructor_profile)

    else:
        courses = Course.objects.none()

    return render(request, 'assignments/assignment_list.html', {
        'courses': courses
    })


def course_assignments(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assignments = Assignment.objects.filter(course=course)

    return render(request, 'assignments/course_assignment.html', {
        'course': course,
        'assignments': assignments
    })


def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('assignment_list')

    else:
        form = AssignmentForm()

    return render(request, 'assignments/create_assignment.html', {
        'form': form
    })