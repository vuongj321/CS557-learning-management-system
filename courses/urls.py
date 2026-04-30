from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='home'),
    path('create/', views.create_course, name='create_course'),
    path('enroll/', views.enroll_course, name='enroll_course'),
    path('<int:course_id>/', views.view_course, name='view_course'),
]