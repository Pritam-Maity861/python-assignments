from utils import calculate_age, days_between_dates, is_leap_year, get_day_of_week

try:
    dob = input("Enter DOB: ")
    print("Age:", calculate_age(dob))
    print("Day:", get_day_of_week(dob))
    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")
    print("Days between dates:", days_between_dates(date1, date2))
    year = int(input("Enter year: "))
    print("Leap year:", is_leap_year(year))
except ValueError as error:
    print("Error:", error)
