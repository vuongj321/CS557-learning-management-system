from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request, 'courses/home.html')

def create_course(request):
    return render(request, 'courses/create_course.html')

def enroll_course(request):
    return render(request, 'courses/enroll_course.html')