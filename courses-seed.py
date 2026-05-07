import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_management_system.settings')
django.setup()

from courses.models import Term, Department

TERMS = [
    {'name': 'Fall 2026', 'start_date': '2026-09-01', 'end_date': '2026-12-20'},
    {'name': 'Spring 2027', 'start_date': '2027-01-15', 'end_date': '2027-05-15'},
    {'name': 'Summer 2027', 'start_date': '2027-06-01', 'end_date': '2027-08-15'},
]

DEPARTMENTS = [
    {'name': 'Computer Science'},
    {'name': 'Mathematics'},
    {'name': 'Physics'},
    {'name': 'Chemistry'},
    {'name': 'Biology'},
    {'name': 'English'},
    {'name': 'History'},
    {'name': 'Psychology'},
    {'name': 'Economics'},
    {'name': 'Sociology'},
]

def seed_terms():
    for term_data in TERMS:
        Term.objects.create(**term_data)
    print("Terms seeded successfully.")

def seed_departments():
    for dept_data in DEPARTMENTS:
        Department.objects.create(**dept_data)
    print("Departments seeded successfully.")

if __name__ == "__main__":
    seed_terms()
    seed_departments()