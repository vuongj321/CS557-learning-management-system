from django.db import models
from assignments.models import Submission

class Grade(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)
