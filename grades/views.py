from django.shortcuts import render, redirect

from accounts.models import StudentProfile
from assignments.models import Assignment
from courses.models import Course
from grades.models import AssignmentGrade


# Create your views here.
def grades(request):
    user = request.user
    if user.is_student():
        # Retrieve all courses enrolled in
        profile = StudentProfile.objects.get(user=user)
        courses = Course.objects.filter(students=profile)
    return render(request, 'viewgrades.html', {'courses': courses, 'student':profile.user.username})

def course_grades(request, course_id):
    user = request.user
    if user.is_student():
        profile = StudentProfile.objects.get(user=user)
    course = Course.objects.get(id=course_id)
    assignments = Assignment.objects.filter(course=course)
    assignment_grades = []
    for assignment in assignments:
        grade = AssignmentGrade.objects.filter(assignment=assignment, student=profile).first()
        assignment_grades.append({'assignment':assignment, 'grade':grade})
    return render(request, 'view_course_grades.html', {'course': course, 'student': profile, 'assignment_grades': assignment_grades})

def grade_assignment(request, assignment_id, student_id):
    assignment = Assignment.objects.get(id=assignment_id)
    student = StudentProfile.objects.get(id=student_id)
    grade = AssignmentGrade.objects.get_or_create(assignment=assignment, student=student)

    if request.method == 'POST':
        points = request.post.get('points_earned')
        grade.points_earned = points
        grade.save()
        return redirect('grades:course_grades', course_id=assignment.course.id)

    return render(request, 'grade_assignment.html', {'grade': grade})
