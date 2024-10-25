"""
deadlines.py - This module handles all operations related to deadlines.
"""

import json
import os
from datetime import datetime

DEADLINE_FILE = 'deadlines.json'

def read_deadlines(deadline_file=DEADLINE_FILE):
    """Read deadlines from a JSON file."""
    if not os.path.exists(deadline_file):
        return []
    with open(deadline_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_deadlines(deadlines, deadline_file=DEADLINE_FILE):
    """Write the list of deadlines to the JSON file."""
    with open(deadline_file, 'w', encoding='utf-8') as file:
        json.dump(deadlines, file)

def add_deadline(task, time, deadline_file=DEADLINE_FILE):
    """Saves deadline to a local file for later use."""
    deadlines = read_deadlines(deadline_file)
    max_id = max((d['id'] for d in deadlines), default=0)
    deadline_id = max_id + 1
    deadlines.append({'id': deadline_id, 'task': task, 'time': time})
    write_deadlines(deadlines, deadline_file)
    print(f"Added deadline: Task - '{task}', Time - '{time}' with ID - {deadline_id}")

def remove_deadline(deadline_id, deadline_file=DEADLINE_FILE):
    """Removes deadline given an ID."""
    deadlines = read_deadlines(deadline_file)
    deadlines = [d for d in deadlines if d['id'] != deadline_id]
    write_deadlines(deadlines, deadline_file)
    print(f"Removed deadline with ID: {deadline_id}")

def remove_all(deadline_file=DEADLINE_FILE):
    """Clears deadline file."""
    if os.path.exists(deadline_file):
        os.remove(deadline_file)
        print("Removed all deadlines.")
    else:
        print("No deadlines to remove.")

def remove_past(deadline_file=DEADLINE_FILE):
    """Clears deadlines in the past."""
    deadlines = read_deadlines(deadline_file)
    current_time = datetime.now().strftime("%H:%M")  # Assuming time format HH:MM
    deadlines = [d for d in deadlines if d['time'] > current_time]
    write_deadlines(deadlines, deadline_file)
    print("Removed past deadlines.")
