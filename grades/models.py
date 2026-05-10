from django.db import models
from assignments.models import Assignment

# Create your models here.
class AssignmentGrade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)
