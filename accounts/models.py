from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def is_instructor(self):
        return self.role == 'instructor'

    def is_student(self):
        return self.role == 'student'


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    # Add additional fields for student profile if needed

    def __str__(self):
        return f"StudentProfile({self.user.username})"


class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor_profile')
    # Add additional fields for instructor profile if needed

    def __str__(self):
        return f"InstructorProfile({self.user.username})"
