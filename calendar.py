import calendar
from termcolor import colored

def print_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(firstweekday=0)  # 0 means Sunday is the first day of the week

    # Generate the month's calendar as a matrix (list of lists)
    month_cal = cal.monthdayscalendar(year, month)

    # Print the header (days of the week)
    header = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    print(" ".join(header))

    # Print the days of the month
    for week in month_cal:
        week_str = ""
        for day in week:
            if day == 0:  # Day 0 means this day is not in the current month
                week_str += "   "
            elif week.index(day) == 6:  # Sunday is the last day in the list
                week_str += colored(f"{day:2}", 'red') + " "
            else:
                week_str += f"{day:2} "
        print(week_str)

# Example usage
year = 2024
month = 7
print_calendar(year, month)
