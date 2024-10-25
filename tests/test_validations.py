'''
Test main.py input validation
'''

import pytest
import click
from deadline_wizard.main import validate_time, validate_task

def test_validate_time():
    '''
    Test for Validate time format for -t argument.
    '''
    assert validate_time('12:30') == '12:30'
    assert validate_time('12:30 PM') == '12:30 PM'
    assert validate_time('1230') == '1230'

    # Check click.BadParameter-Exception is thrown with invalid input
    with pytest.raises(click.BadParameter):
        validate_time(None)  # Example invalid input

    with pytest.raises(click.BadParameter):
        validate_time('invalid_time')  # Example invalid time format

def test_validate_task():
    '''
    Test for task input validation
    '''
    assert validate_task('My Task') == 'My Task'

    # Check overly long inputs
    with pytest.raises(click.BadParameter):
        validate_task('A very long task exceeding the length limit. '
        'It is definitely longer than 100 characters lalalalalalalalalalalalala...')
