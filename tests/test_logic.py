import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic import generate_password

def test_password_length():

    password = generate_password(10)

    assert len(password) == 10


def test_numbers_included():

    password = generate_password(20, use_numbers=True, use_symbols=False)

    assert any(char.isdigit() for char in password)


def test_symbols_included():

    password = generate_password(20, use_numbers=False, use_symbols=True)

    assert any(not char.isalnum() for char in password)


def test_no_numbers():

    password = generate_password(20, use_numbers=False)

    assert not any(char.isdigit() for char in password)


def test_invalid_length():

    try:
        generate_password(0)
    except ValueError:
        assert True