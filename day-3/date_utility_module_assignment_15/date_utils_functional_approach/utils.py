from datetime import datetime, date


def calculate_age(dob):
    try:
        dob = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    today = date.today()
    if dob > today:
        raise ValueError("Date of birth cannot be in the future.")
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


def days_between_dates(date1, date2):
    try:
        date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        date2 = datetime.strptime(date2, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    return abs((date2 - date1).days)


def is_leap_year(year):
    if year < 1:
        raise ValueError("Year must be positive.")
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_day_of_week(date_string):
    try:
        date_value = datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    return date_value.strftime("%A")
