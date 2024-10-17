import calendar
from termcolor import colored


def print_calendar(year, month):
    # Create a TextCalendar instance with Sunday as the first day of the week
    cal = calendar.TextCalendar(firstweekday=6)

    # Generate the month's calendar as a matrix (list of lists)
    month_cal = cal.monthdayscalendar(year, month)

    # Print the header (days of the week)
    header = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    print(" ".join(header))

    # Print the days of the month
    for week in month_cal:
        week_str = ""
        for i, day in enumerate(week):
            if day == 0:  # Day 0 means this day is not in the current month
                week_str += "   "
            elif i == 6:  # Sunday is the last day in the list and should be colored red
                week_str += colored(f"{day:2}", "red") + " "
            else:
                week_str += f"{day:2} "
        print(week_str)


# Example usage
year = 2024
month = 7
print_calendar(year, month)
