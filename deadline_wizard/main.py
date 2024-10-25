"""
Main module for the Deadline Tracker CLI, handling command-line input and validating user inputs.
"""

import click
import re
from deadline_wizard.deadlines import add_deadline, remove_deadline, remove_all, remove_past

MAX_TASK_LENGTH = 100  # Maximum characters for task
TIME_FORMATS = [
    r'^\d{1,2}:\d{2}$',  # HH:MM
    r'^\d{1,2}:\d{2} [AP]M$',  # HH:MM AM/PM
    r'^\d{4}$'  # HHMM (e.g. 1230 for 12:30)
]

def validate_time(ctx, param, value):
    """Validate correct time format."""
    if value is None:
        click.echo("Time can't be None.")
        raise click.BadParameter('Time must be provided.')
    
    # Check time format
    for fmt in TIME_FORMATS:
        if re.match(fmt, value):
            return value
            
    # Time format not in list
    raise click.BadParameter('Time format has to be either HH:MM, HH:MM AM/PM or HHMM.')

def validate_task(ctx, param, value):
    """Validate Task-String."""
    if len(value) > MAX_TASK_LENGTH:
        raise click.BadParameter(f'Task description length must not exceed {MAX_TASK_LENGTH} characters.')
    return value

@click.group()
def cli():
    """A CLI tool for managing deadlines."""
    pass

@cli.command(name='set')
@click.argument('task', type=str, callback=validate_task)
@click.option('--time', '-t', required=True, type=str, help='Time for deadline (HH:MM, HH:MM AM/PM or HHMM)', callback=validate_time)
def set_deadline(task, time):
    """Set a new deadline for the given TASK."""
    add_deadline(task, time)
    click.echo(f'Deadline set for: {task} at {time}')

@cli.command(name='delete')
@click.argument('deadline_id', type=int)
def delete(deadline_id):
    """Delete a deadline by ID."""
    remove_deadline(deadline_id)
    click.echo(f'Deleted deadline with ID: {deadline_id}')

@cli.command(name='clear_all')
def clear_all():
    """Clear all deadlines."""
    remove_all()
    click.echo("Cleared all deadlines.")

@cli.command(name='clear_past')
def clear_past():
    """Clear past deadlines."""
    remove_past()
    click.echo("Cleared past deadlines.")

@cli.command(name='history')
def history():
    """Show past deadlines."""
    click.echo("Showing history of past deadlines (not implemented yet).")

@cli.command(name='summary')
def summary():
    """Show a summary of upcoming deadlines."""
    click.echo("Showing summary of upcoming deadlines (not implemented yet).")

@cli.command(name="live")
def live():
    """Show upcoming deadlines and time delta. Updates every second."""
    click.echo("Showing upcoming deadlines (not implemented yet).")

if __name__ == '__main__':
    cli()
