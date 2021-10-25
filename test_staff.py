import pytest
import json
import os
import Staff

def test_change_grade(staff):
    # Pull from user database. Store all users.
    fp = open('Data/users.json')
    users = json.load(fp)
    staff.users = users
    fp.close()

    # Change grade for valid user.
    username = 'akend3'
    course = 'comp_sci'
    assignment_name = 'assignment1'
    grade = 69

    # Attempt to change the users grade.
    staff.change_grade(username, course, assignment_name, grade)

    # The database must reflect a change to the correct username, in the correct course, for the correct assignment grade.
    assert users[username]['courses'][course][assignment_name]['grade'] == grade

def test_change_invalid_grade(staff):
    # Pull from user database. Store all users.
    fp = open('Data/users.json')
    users = json.load(fp)
    staff.users = users
    fp.close()

    # Change to invalid grade for valid user.
    username = 'akend3'
    course = 'comp_sci'
    assignment_name = 'assignment1'
    grade = -1
    good_grade = users[username]['courses'][course][assignment_name]['grade']

    # Attempt to change the users grade.
    staff.change_grade(username, course, assignment_name, grade)

    # The database must not reflect a change to the grade.
    assert users[username]['courses'][course][assignment_name]['grade'] == good_grade

def test_create_assignment(staff):
    # Pull from course database. Store all courses.
    fp = open('Data/courses.json')
    courses = json.load(fp)
    staff.all_courses = courses
    fp.close()

    # Course and assignment to add.
    course = 'databases'
    assignment_name = 'assignment3'
    due_date = '10/24/21'

    # Attempt to create the assignment.
    staff.create_assignment(assignment_name, due_date, course)

    # Verify that the correct course in the database has an the correct assignment and corresponding due date.
    assert courses[course]['assignments'][assignment_name]['due_date'] == due_date

@pytest.fixture
def staff():
    os.system('python RestoreData.py')
    staff = Staff.Staff()
    return staff