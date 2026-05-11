from django.shortcuts import render, redirect, get_object_or_404

from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm
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


def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    student = request.user.student_profile
    existing = Submission.objects.filter(assignment=assignment, student=student).first()

    if request.method == 'POST' and not existing:
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = student
            submission.status = Submission.Status.SUBMITTED
            submission.save()
            return redirect('course_assignments', course_id=assignment.course.id)
    else:
        form = SubmissionForm()

    return render(request, 'assignments/submit_assignment.html', {
        'form': form,
        'assignment': assignment,
        'existing': existing,
    })