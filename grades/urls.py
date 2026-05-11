from django.urls import path
from . import views

app_name = 'grades'
urlpatterns = [
    path('', views.grades, name='grades'),
    path('course/<int:course_id>', views.course_grades, name='view_course_grades'),
    path('submission/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
]