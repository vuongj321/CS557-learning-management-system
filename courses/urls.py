from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='home'),
    path('create/', views.create_course, name='create_course'),
    path('<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('<int:course_id>/enrollments/', views.manage_enrollments, name='enrollments'),
    path('<int:course_id>/', views.view_course, name='view_course'),   
]