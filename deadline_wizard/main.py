import click
import re
from .deadlines import add_deadline

MAX_TASK_LENGTH = 100  # Maximum characters for time
TIME_FORMATS = [
    r'^\d{1,2}:\d{2}$',  # HH:MM
    r'^\d{1,2}:\d{2} [AP]M$',  # HH:MM AM/PM
    r'^\d{4}$'  # HHMM (z.B. 1230 für 12:30)
]

def validate_time(ctx, param, value):
    """Validate correct time format"""
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

@click.command()
@click.argument('task', type=str, callback=validate_task)
@click.option('--time', '-t', required=True, type=str, help='Time for deadline (HH:MM, HH:MM AM/PM oder HHMM)', callback=validate_time)
def set_deadline(task, time):
    """Set a new deadline for the given TASK."""
    add_deadline(task, time)
    click.echo(f'Deadline set for: {task}')

if __name__ == '__main__':
    set_deadline()
