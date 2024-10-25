'''
Tests the functionality of deadlines.py.
'''

import os
import json
from datetime import datetime, timedelta
import pytest
from deadline_wizard.deadlines import (
    add_deadline,
    remove_deadline,
    remove_all,
    remove_past,
    read_deadlines,
    write_deadlines
)

TEST_DEADLINE_FILE = 'test_deadlines.json'

@pytest.fixture
def setup_deadline_file():
    """Fixture to set up and tear down the test_deadlines.json file."""
    # Remove the test file if it exists before the test
    if os.path.exists(TEST_DEADLINE_FILE):
        os.remove(TEST_DEADLINE_FILE)
    yield
    # Remove the test file after the test
    if os.path.exists(TEST_DEADLINE_FILE):
        os.remove(TEST_DEADLINE_FILE)

def test_add_deadline(setup_deadline_file):
    """Test adding a deadline."""
    add_deadline('Test Task', '18:00', TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)
    assert len(deadlines) == 1
    assert deadlines[0]['task'] == 'Test Task'
    assert deadlines[0]['time'] == '18:00'

def test_remove_deadline(setup_deadline_file):
    """Test removing a deadline."""
    add_deadline('Test Task', '18:00', TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)
    deadline_id = deadlines[0]['id']

    remove_deadline(deadline_id, TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)
    assert len(deadlines) == 0

def test_remove_all(setup_deadline_file):
    """Test removing all deadlines."""
    add_deadline('Test Task 1', '18:00', TEST_DEADLINE_FILE)
    add_deadline('Test Task 2', '19:00', TEST_DEADLINE_FILE)

    remove_all(TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)
    assert len(deadlines) == 0

def test_remove_past(setup_deadline_file):
    """Test removing past deadlines."""
    # Adding a past deadline
    past_time = (datetime.now() - timedelta(minutes=1)).strftime("%H:%M")
    add_deadline('Past Task', past_time, TEST_DEADLINE_FILE)

    # Adding a future deadline
    future_time = (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")
    add_deadline('Future Task', future_time, TEST_DEADLINE_FILE)

    # Remove past deadlines
    remove_past(TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)

    # Check that only the future task remains
    assert len(deadlines) == 1
    assert deadlines[0]['task'] == 'Future Task'

def test_write_deadlines(setup_deadline_file):
    """Test writing deadlines to the test file."""
    deadlines = [{'id': 1, 'task': 'Test Task', 'time': '18:00'}]
    write_deadlines(deadlines, TEST_DEADLINE_FILE)
    with open(TEST_DEADLINE_FILE, 'r', encoding='utf-8') as file:
        saved_deadlines = json.load(file)

    assert len(saved_deadlines) == 1
    assert saved_deadlines[0]['task'] == 'Test Task'

def test_read_deadlines(setup_deadline_file):
    """Test reading deadlines from the test file."""
    add_deadline('Test Task', '18:00', TEST_DEADLINE_FILE)
    deadlines = read_deadlines(TEST_DEADLINE_FILE)
    assert len(deadlines) == 1
    assert deadlines[0]['task'] == 'Test Task'
