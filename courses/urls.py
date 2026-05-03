from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='home'),
    path('create/', views.create_course, name='create_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('enroll/', views.enroll_course, name='enroll_course'),
    path('<int:course_id>/', views.view_course, name='view_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]