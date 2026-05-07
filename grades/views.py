from django.shortcuts import render

from accounts.models import StudentProfile
from courses.models import Course


# Create your views here.
def grades(request):
    user = request.user
    if user.is_student():
        # Retrieve all courses enrolled in
        profile = StudentProfile.objects.get(user=user)
        courses = Course.objects.filter(students=profile)
    return render(request, 'viewgrades.html', {'courses': courses, 'student':profile.user.username})