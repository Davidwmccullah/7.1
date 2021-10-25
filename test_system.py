import pytest
import json
import os
import System

def test_login(system):
    # Get users from database.
    fp = open('Data/users.json')
    users = json.load(fp)
    fp.close()

    # Set valid login.
    username = 'goggins'
    password = 'augurrox'

    # Attempt login.
    system.login(username, password)

    # Verify correct user data.
    assert system.usr.name == username
    assert system.usr.courses == users[username]['courses']
    assert system.usr.password == password

def test_check_password(system):
    # Set good username.
    username = 'goggins'

    # Set bad passwords.
    passwords = [
        'null',
        'nan',
        '4w3s0m3',
        '0000',
        ' ',
        '',
        '\n',
        0,
    ]

    # Test bad passwords against good username. Expects false.
    for password in passwords:
        assert system.check_password(username, password) == False

    # Test correct password. Expects true.
    password = 'augurrox'
    assert system.check_password(username, password) == True

def test_padded_password(system):
    # Set good username.
    username = 'goggins'

    # Set padded passwords.
    passwords = [
        ' augurrox',
        ' augurrox ',
        'augurrox '
    ]

    # Test padded passwords against good username. Expects passwords to be trimmed and accepted.
    for password in passwords:
        assert system.check_password(username, password)

@pytest.fixture
def system():
    os.system('python RestoreData.py')
    system = System.System()
    system.load_data()
    return system

