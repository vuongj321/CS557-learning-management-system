from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('create/', views.create_course, name='create_course'),
    path('enroll/', views.enroll_course, name='enroll_course'),
]