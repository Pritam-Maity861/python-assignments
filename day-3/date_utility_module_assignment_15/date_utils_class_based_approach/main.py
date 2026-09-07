from utils import DateUtils

utils = DateUtils()

try:
    dob = input("Enter DOB: ")
    print("Age:", utils.calculate_age(dob))
    print("Day:", utils.get_day_of_week(dob))
    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")
    print("Days between dates:", utils.days_between_dates(date1, date2))
    year = int(input("Enter year: "))
    print("Leap year:", utils.is_leap_year(year))
except ValueError as error:
    print("Error:", error)
