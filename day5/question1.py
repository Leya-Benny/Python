def main():
    month = int(input("Enter the month in the numeric form:"))
    day = int(input("Enter the day in numeric form:"))
    year= int(input("Enter the year in two numeric digits (for example: 98, 20, 21):"))

    if month < 1 or month > 12:
        print("Month: Error: Invalid Month Input")
    elif year < 0 or year > 99:
        print("Year: Error: Invalid Year Input")
    elif day < 1 or (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30) or (month not in [2, 4, 6, 9, 11] and day > 31):
        print("Day: Error: There is no such date in the calendar.")
    else:
        print(f"The date you entered is: {month:02d}/{day:02d}/{year:02d}")
        print("Success: Congratulations! You entered a correct date.")
if __name__ == "__main__":
  main()