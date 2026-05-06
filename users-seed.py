import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_management_system.settings')
django.setup()

from accounts.models import User, StudentProfile, InstructorProfile

INSTRUCTORS = [
    {'username': 'prof_smith',   'first_name': 'John',    'last_name': 'Smith',    'email': 'smith@school.edu'},
    {'username': 'prof_jones',   'first_name': 'Emily',   'last_name': 'Jones',    'email': 'jones@school.edu'},
    {'username': 'prof_patel',   'first_name': 'Raj',     'last_name': 'Patel',    'email': 'patel@school.edu'},
    {'username': 'prof_chen',    'first_name': 'Linda',   'last_name': 'Chen',     'email': 'chen@school.edu'},
    {'username': 'prof_nguyen',  'first_name': 'David',   'last_name': 'Nguyen',   'email': 'nguyen@school.edu'},
]

STUDENTS = [
    {'username': 'alice_j',   'first_name': 'Alice',   'last_name': 'Johnson',    'email': 'alice.johnson@school.edu'},
    {'username': 'bob_m',     'first_name': 'Bob',     'last_name': 'Martinez',   'email': 'bob.martinez@school.edu'},
    {'username': 'carol_w',   'first_name': 'Carol',   'last_name': 'Wilson',     'email': 'carol.wilson@school.edu'},
    {'username': 'dan_b',     'first_name': 'Daniel',  'last_name': 'Brown',      'email': 'daniel.brown@school.edu'},
    {'username': 'eva_d',     'first_name': 'Eva',     'last_name': 'Davis',      'email': 'eva.davis@school.edu'},
    {'username': 'frank_t',   'first_name': 'Frank',   'last_name': 'Taylor',     'email': 'frank.taylor@school.edu'},
    {'username': 'grace_a',   'first_name': 'Grace',   'last_name': 'Anderson',   'email': 'grace.anderson@school.edu'},
    {'username': 'henry_t',   'first_name': 'Henry',   'last_name': 'Thomas',     'email': 'henry.thomas@school.edu'},
    {'username': 'iris_m',    'first_name': 'Iris',    'last_name': 'Moore',      'email': 'iris.moore@school.edu'},
    {'username': 'jack_h',    'first_name': 'Jack',    'last_name': 'Harris',     'email': 'jack.harris@school.edu'},
    {'username': 'karen_c',   'first_name': 'Karen',   'last_name': 'Clark',      'email': 'karen.clark@school.edu'},
    {'username': 'liam_l',    'first_name': 'Liam',    'last_name': 'Lewis',      'email': 'liam.lewis@school.edu'},
    {'username': 'mia_r',     'first_name': 'Mia',     'last_name': 'Robinson',   'email': 'mia.robinson@school.edu'},
    {'username': 'noah_w',    'first_name': 'Noah',    'last_name': 'Walker',     'email': 'noah.walker@school.edu'},
    {'username': 'olivia_h',  'first_name': 'Olivia',  'last_name': 'Hall',       'email': 'olivia.hall@school.edu'},
    {'username': 'peter_a',   'first_name': 'Peter',   'last_name': 'Allen',      'email': 'peter.allen@school.edu'},
    {'username': 'quinn_y',   'first_name': 'Quinn',   'last_name': 'Young',      'email': 'quinn.young@school.edu'},
    {'username': 'rachel_k',  'first_name': 'Rachel',  'last_name': 'King',       'email': 'rachel.king@school.edu'},
    {'username': 'sam_w',     'first_name': 'Samuel',  'last_name': 'Wright',     'email': 'samuel.wright@school.edu'},
    {'username': 'tina_s',    'first_name': 'Tina',    'last_name': 'Scott',      'email': 'tina.scott@school.edu'},
    {'username': 'uma_g',     'first_name': 'Uma',     'last_name': 'Green',      'email': 'uma.green@school.edu'},
    {'username': 'victor_b',  'first_name': 'Victor',  'last_name': 'Baker',      'email': 'victor.baker@school.edu'},
    {'username': 'wendy_n',   'first_name': 'Wendy',   'last_name': 'Nelson',     'email': 'wendy.nelson@school.edu'},
    {'username': 'xander_c',  'first_name': 'Xander',  'last_name': 'Carter',     'email': 'xander.carter@school.edu'},
    {'username': 'yara_m',    'first_name': 'Yara',    'last_name': 'Mitchell',   'email': 'yara.mitchell@school.edu'},
    {'username': 'zoe_p',     'first_name': 'Zoe',     'last_name': 'Perez',      'email': 'zoe.perez@school.edu'},
    {'username': 'adam_r',    'first_name': 'Adam',    'last_name': 'Roberts',    'email': 'adam.roberts@school.edu'},
    {'username': 'bella_t',   'first_name': 'Bella',   'last_name': 'Turner',     'email': 'bella.turner@school.edu'},
    {'username': 'carlos_p',  'first_name': 'Carlos',  'last_name': 'Phillips',   'email': 'carlos.phillips@school.edu'},
    {'username': 'diana_c',   'first_name': 'Diana',   'last_name': 'Campbell',   'email': 'diana.campbell@school.edu'},
    {'username': 'ethan_p',   'first_name': 'Ethan',   'last_name': 'Parker',     'email': 'ethan.parker@school.edu'},
    {'username': 'fiona_e',   'first_name': 'Fiona',   'last_name': 'Evans',      'email': 'fiona.evans@school.edu'},
    {'username': 'george_e',  'first_name': 'George',  'last_name': 'Edwards',    'email': 'george.edwards@school.edu'},
    {'username': 'hannah_c',  'first_name': 'Hannah',  'last_name': 'Collins',    'email': 'hannah.collins@school.edu'},
    {'username': 'ivan_s',    'first_name': 'Ivan',    'last_name': 'Stewart',    'email': 'ivan.stewart@school.edu'},
    {'username': 'julia_m',   'first_name': 'Julia',   'last_name': 'Morris',     'email': 'julia.morris@school.edu'},
    {'username': 'kevin_r',   'first_name': 'Kevin',   'last_name': 'Rogers',     'email': 'kevin.rogers@school.edu'},
    {'username': 'luna_r',    'first_name': 'Luna',    'last_name': 'Reed',       'email': 'luna.reed@school.edu'},
    {'username': 'mason_c',   'first_name': 'Mason',   'last_name': 'Cook',       'email': 'mason.cook@school.edu'},
    {'username': 'nora_b',    'first_name': 'Nora',    'last_name': 'Bailey',     'email': 'nora.bailey@school.edu'},
    {'username': 'oscar_b',   'first_name': 'Oscar',   'last_name': 'Bell',       'email': 'oscar.bell@school.edu'},
    {'username': 'paula_m',   'first_name': 'Paula',   'last_name': 'Murphy',     'email': 'paula.murphy@school.edu'},
    {'username': 'quentin_r', 'first_name': 'Quentin', 'last_name': 'Rivera',     'email': 'quentin.rivera@school.edu'},
    {'username': 'rose_c',    'first_name': 'Rose',    'last_name': 'Cooper',     'email': 'rose.cooper@school.edu'},
    {'username': 'steve_r',   'first_name': 'Steve',   'last_name': 'Richardson', 'email': 'steve.richardson@school.edu'},
    {'username': 'tara_c',    'first_name': 'Tara',    'last_name': 'Cox',        'email': 'tara.cox@school.edu'},
    {'username': 'ulrich_h',  'first_name': 'Ulrich',  'last_name': 'Howard',     'email': 'ulrich.howard@school.edu'},
    {'username': 'vera_w',    'first_name': 'Vera',    'last_name': 'Ward',       'email': 'vera.ward@school.edu'},
    {'username': 'will_t',    'first_name': 'William', 'last_name': 'Torres',     'email': 'william.torres@school.edu'},
    {'username': 'xena_p',    'first_name': 'Xena',    'last_name': 'Peterson',   'email': 'xena.peterson@school.edu'},
]

DEFAULT_PASSWORD = 'pass1234'

def seed():
    print("Seeding instructors...")
    for data in INSTRUCTORS:
        if User.objects.filter(username=data['username']).exists():
            print(f"  Skipping {data['username']} (already exists)")
            continue
        user = User.objects.create_user(
            username=data['username'],
            password=DEFAULT_PASSWORD,
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data.get('email', ''),
            role='instructor',
        )
        InstructorProfile.objects.create(user=user)
        print(f"  Created instructor: {user.username}")

    print("\nSeeding students...")
    for data in STUDENTS:
        if User.objects.filter(username=data['username']).exists():
            print(f"  Skipping {data['username']} (already exists)")
            continue
        user = User.objects.create_user(
            username=data['username'],
            password=DEFAULT_PASSWORD,
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data.get('email', ''),
            role='student',
        )
        StudentProfile.objects.create(user=user)
        print(f"  Created student: {user.username}")

    print("\nDone. All users have password: pass1234")

if __name__ == '__main__':
    seed()