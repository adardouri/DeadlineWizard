import json
import os
from datetime import datetime

DEADLINE_FILE = 'deadlines.json'

def read_deadlines():
    """Read deadlines from a JSON file."""
    if not os.path.exists(DEADLINE_FILE):
        return []
    with open(DEADLINE_FILE, 'r') as file:
        return json.load(file)

def write_deadlines(deadlines):
    """Write the list of deadlines to the JSON file."""
    with open(DEADLINE_FILE, 'w') as file:
        json.dump(deadlines, file)

def add_deadline(task, time):
    """Saves deadline to a local file for later use."""
    deadlines = read_deadlines()
    deadline_id = len(deadlines) + 1  # Simple ID assignment
    deadlines.append({'id': deadline_id, 'task': task, 'time': time})
    write_deadlines(deadlines)
    print(f"Added deadline: Task - '{task}', Time - '{time}'")

def remove_deadline(deadline_id):
    """Removes deadline given an ID."""
    deadlines = read_deadlines()
    deadlines = [d for d in deadlines if d['id'] != deadline_id]
    write_deadlines(deadlines)
    print(f"Removed deadline with ID: {deadline_id}")

def remove_all():
    """Clears deadline file."""
    if os.path.exists(DEADLINE_FILE):
        os.remove(DEADLINE_FILE)
        print("Removed all deadlines.")
    else:
        print("No deadlines to remove.")

def remove_past():
    """Clears deadlines in the past."""
    deadlines = read_deadlines()
    current_time = datetime.now().strftime("%H:%M")  # Assuming time format HH:MM
    deadlines = [d for d in deadlines if d['time'] > current_time]
    write_deadlines(deadlines)
    print("Removed past deadlines.")
