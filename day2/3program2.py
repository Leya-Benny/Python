
#Obtain date, month and year as inputs from user and find the next date.

def next_date(day, month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < days_in_months[month - 1]:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return day, month, year

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
next_day, next_month, next_year = next_date(day, month, year)
print(f"The next date is: {next_day}/{next_month}/{next_year}")