import pytest

@pytest.fixture
def my_fixture():
    """
    This is the docstring for the my_fixture fixture.
    This will show up in pytest --fixtures
    """
    return 42

@pytest.fixture
def captured_print(capsys):
    print("hello")
