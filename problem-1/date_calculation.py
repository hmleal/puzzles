import datetime


WEDNESDAY = 2
SATURDAY = 5


def next_draw(date=None):
    """
    Return the next draw lottery date.

    If the passed date gt 08:00PM returns the next day of lottery draw.

    Args:
      date (str): Datetime string in this format "%Y-%m-%d %H:%M"

    Returns:
      str: The date of the next draw.
    """
    if date is None:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')

    if date.time() >= datetime.time(20, 0):
        date += datetime.timedelta(days=1)

    while date.weekday() not in [WEDNESDAY, SATURDAY]:
        date += datetime.timedelta(days=1)

    return date.strftime('Next draw will be at: %d, %b %Y at 8:00PM')
