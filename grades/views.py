from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import normalize_newlines

from accounts.models import StudentProfile
from assignments.models import Assignment, Submission
from courses.models import Course
from grades.models import Grade


# Create your views here.
def grades(request):
    user = request.user
    if user.is_student():
        profile = StudentProfile.objects.get(user=user)
        courses = Course.objects.filter(students=profile)
        return render(request, 'viewGrades.html', {'courses': courses, 'student':profile.user.username})
    return redirect('home')

def course_grades(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    if user.is_student():
        profile = StudentProfile.objects.get(user=user)
        assignments = Assignment.objects.filter(course=course)
        assignment_grades = []

        for assignment in assignments:
            submission = Submission.objects.filter(assignment=assignment, student=profile).first()
            grade = None
            if submission and submission.status == Submission.Status.GRADED:
                grade = Grade.objects.filter(submission=submission).first()

            assignment_grades.append({'assignment':assignment, 'submission':submission, 'grade':grade})

        return render(request, 'view_course_grades.html', {'course':course, 'student': profile, 'assignment_grades':assignment_grades})
    else:
        submissions = Submission.objects.filter(assignment__course=course).select_related('assignment', 'student')
        return render(request, 'view_course_grades.html', {
            'course': course,
            'submissions': submissions,
            'is_instructor': True
        })

def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    grade, created = Grade.objects.get_or_create(submission=submission)

    if request.method == 'POST':
        score = request.POST.get('score')
        feedback = request.POST.get('feedback')

        grade.score = score
        grade.feedback = feedback
        grade.save()

        submission.status = Submission.Status.GRADED
        submission.save()

        return redirect('grades:instructor_course_submissions', course_id=submission.assignment.course.id)

    return render(request, 'grade_assignment.html', {'grade': grade,'submission': submission
    })