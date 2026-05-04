from django.db import models

class Term(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey('accounts.InstructorProfile', on_delete=models.CASCADE)
    students = models.ManyToManyField('accounts.StudentProfile', through='Enrollment')
    description = models.TextField()
    credits = models.PositiveIntegerField()
    number_of_seats = models.PositiveIntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.name}"