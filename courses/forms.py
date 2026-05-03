from django import forms
from courses.models import Department, Term

class CreateCourseForm(forms.Form):
    course_name = forms.CharField(max_length=100)
    course_description = forms.CharField(widget=forms.Textarea)
    credits = forms.IntegerField(min_value=1, max_value=5)
    number_of_seats = forms.IntegerField(min_value=1, max_value=100)
    term = forms.ModelChoiceField(queryset=Term.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)
