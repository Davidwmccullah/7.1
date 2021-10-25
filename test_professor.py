import pytest
import json
import os
import Professor

def test_add_student(professor):
    # Add user to new course.
    username = 'yted91'
    course = 'databases'

    # Attempt to add student.
    professor.add_student(username, course)

    # The user database must have the correct course for the user.
    assert course in professor.users[username]['courses']

def test_add_student_to_invalid_course(professor):
    # Set course to a course not led by this professor.
    username = 'yted91'
    course = 'comp_sci'

    # Attempt to add student.
    professor.add_student(username, course)

    # The user database must not have this course for the user.
    assert course not in professor.users[username]['courses']

def test_drop_student(professor):
    # Remove user from existing course.
    username = 'akend3'
    course = 'databases'

    # Attempt to drop student.
    professor.drop_student(username, course)

    # The user database must not have the course for the user.
    assert course not in professor.users[username]['courses']

def test_drop_student_from_invalid_course(professor):
    # Set course to a course not led by this professor.
    username = 'akend3'
    course = 'comp_sci'

    # Attempt to drop student.
    professor.drop_student(username, course)

    # The user database must still have the course for the user.
    assert course in professor.users[username]['courses']

@pytest.fixture
def professor():
    os.system('python RestoreData.py')
    fp = open('Data/users.json')
    users = json.load(fp)
    fp.close()

    fp = open('Data/courses.json')
    courses = json.load(fp)
    fp.close()

    username = 'goggins'
    professor = Professor.Professor(username, users, courses)
    professor.users = users
    professor.all_courses = courses
    return professor