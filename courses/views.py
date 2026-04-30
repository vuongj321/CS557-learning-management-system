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
            instructor_profile = InstructorProfile.objects.get(user=request.user)
            Course.objects.create(
                name=course_name,
                description=course_description,
                credits=credits,
                number_of_seats=number_of_seats,
                term=term,
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
    return render(request, 'courses/view_course.html', {'course': course})