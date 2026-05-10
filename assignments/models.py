from django.db import models
from courses.models import Course
from accounts.models import StudentProfile


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    points_possible = models.IntegerField(default=100)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        SUBMITTED = 'submitted'
        GRADED = 'graded'
        
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    submission_text = models.TextField()
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=20)