from django.shortcuts import redirect, render

from accounts.models import InstructorProfile, StudentProfile
from courses.forms import CreateCourseForm
from courses.models import Course

# Create your views here.
def courses(request):
    user = request.user
    # Retrieve all course for the logged-in user
    if user.is_instructor():
        profile = InstructorProfile.objects.get(user=user)
        courses = Course.objects.filter(instructor=profile)
    else:
        profile = StudentProfile.objects.get(user=user)
        courses = Course.objects.filter(students=profile)
    return render(request, 'courses/home.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        # Handle course creation logic here
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            course_name = form.cleaned_data['course_name']
            course_description = form.cleaned_data['course_description']
            credits = form.cleaned_data['credits']
            number_of_seats = form.cleaned_data['number_of_seats']
            term = form.cleaned_data['term']
            department = form.cleaned_data['department']
            instructor_profile = InstructorProfile.objects.get(user=request.user)
            Course.objects.create(
                name=course_name,
                description=course_description,
                credits=credits,
                number_of_seats=number_of_seats,
                term=term,
                department=department,
                instructor=instructor_profile
            )
            return redirect('courses:home')
    else:
        form = CreateCourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

def enroll_course(request):
    return render(request, 'courses/enroll_course.html')

def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    user = request.user

    is_instructor = False
    is_owner = False
    is_enrolled = False
    enrolled_count = course.enrollment_set.count()
    enrollments = course.enrollment_set.select_related('student', 'student__user')

    if user.is_authenticated:
        # determine instructor ownership
        try:
            if hasattr(user, 'instructor_profile') and user.is_instructor():
                is_instructor = True
                instructor_profile = user.instructor_profile
                is_owner = (course.instructor == instructor_profile)
        except InstructorProfile.DoesNotExist:
            is_instructor = False

        # determine student enrollment
        try:
            if hasattr(user, 'student_profile') and user.is_student():
                student_profile = user.student_profile
                is_enrolled = course.enrollment_set.filter(student=student_profile).exists()
        except StudentProfile.DoesNotExist:
            is_enrolled = False

    context = {
        'course': course,
        'is_instructor': is_instructor,
        'is_owner': is_owner,
        'is_enrolled': is_enrolled,
        'enrolled_count': enrolled_count,
        'enrollments': enrollments,
    }

    return render(request, 'courses/view_course.html', context)

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses:home')

def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            course.name = form.cleaned_data['course_name']
            course.description = form.cleaned_data['course_description']
            course.credits = form.cleaned_data['credits']
            course.number_of_seats = form.cleaned_data['number_of_seats']
            course.term = form.cleaned_data['term']
            course.department = form.cleaned_data['department']
            course.save()
            return redirect('courses:view_course', course_id=course.id)
    else:
        initial_data = {
            'course_name': course.name,
            'course_description': course.description,
            'credits': course.credits,
            'number_of_seats': course.number_of_seats,
            'term': course.term,
            'department': course.department
        }
        form = CreateCourseForm(initial=initial_data)
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})