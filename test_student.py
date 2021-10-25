import pytest
import json
import os
import Student

def test_submit_assignment(student):
    # Submit the second databases assignment on a valid date.
    course = 'databases'
    assignment_name = 'assignment2'
    submission = 'test'
    submission_date = '10/23/20'

    # Attempt to submit the assignment.
    student.submit_assignment(course, assignment_name, submission, submission_date)

    # Check that the assignment has been updated.
    assert student.users[student.name]['courses'][course][assignment_name][submission_date] == submission_date
    assert student.users[student.name]['courses'][course][assignment_name][submission] == submission

def test_check_ontime(student):
    # Submission is after the due date.
    submission_date = '10/24/21'
    due_date = '10/23/21'

    # Submission should not be allowed.
    assert not student.check_ontime(submission_date, due_date)

def test_check_invalid_ontime(student):
    # Submission is impossible data.
    submission_date = '99/99/99'
    due_date = '10/23/21'

    # Submission should not be allowed.
    assert not student.check_ontime(submission_date, due_date)

def test_check_grades(student):
    # Checking databases grades.
    course = 'databases'

    # Check the grades.
    grades = student.check_grades(course)

    # Get the grades from the database.
    actual_grades = []
    for assignment in student.users[student.name]['courses'][course]:
        actual_grades.append([assignment, student.users[student.name]['courses'][course][assignment]['grade']])

    # The returned grades must match the grades in the database.
    assert grades == actual_grades

def test_view_assignments(student):
    # Checking databases assignments.
    course = 'databases'

    # Attempt to get the assignments
    assignments = student.view_assignments(course)
   
    # Get the assignments from the database.
    actual_assignments = []
    for assignment in student.all_courses[course]['assignments']:
        actual_assignments.append([assignment, student.all_courses[course]['assignments'][assignment]['due_date']])

    # The returned assignments must match the assignments in the database.
    assert assignments == actual_assignments

@pytest.fixture
def student():
    os.system('python RestoreData.py')
    fp = open('Data/users.json')
    users = json.load(fp)
    fp.close()

    fp = open('Data/courses.json')
    courses = json.load(fp)
    fp.close()

    username = 'hdjsr7'

    student = Student.Student(username, users, courses)
    return student
