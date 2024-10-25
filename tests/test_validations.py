import pytest
import click
from deadline_wizard.main import validate_time, validate_task

def test_validate_time():
    assert validate_time(None, None, '12:30') == '12:30'
    assert validate_time(None, None, '12:30 PM') == '12:30 PM'
    assert validate_time(None, None, '1230') == '1230'

    # Check click.BadParameter-Exception is thrown with invalid input
    with pytest.raises(click.BadParameter):
        validate_time(None, None, None)  # Example invalid input

    with pytest.raises(click.BadParameter):
        validate_time(None, None, 'invalid_time')  # Example invalid time format

def test_validate_task():
    assert validate_task(None, None, 'My Task') == 'My Task'

    # Check overly long inputs
    with pytest.raises(click.BadParameter):
        validate_task(None, None, 'A very long task exceeding the length limit for tasks you should use to trigger.' 
        'It is definitely longer than 100 characters lalalalalalalalalalalalala...')
