#Calorie Intake Tracker
while True:
    start_cal = float(input("Enter your starting daily calorie intake: "))
    if start_cal <= 0:
        print("Error: Please enter a positive value.")
    else:
        break
while True:
    per = float(input("Enter the average daily percentage decrease: "))
    if per <= 0:
        print("Error: Please enter a positive value.")
    else:
        break
while True:
    days = int(input("Enter the number of days for the diet: "))
    if days <= 0:
        print("Error: Please enter a positive value.")
    else:
        break
cal = start_cal
print(f"\nDay 1: {cal:.2f} calories")

for day in range(2, days + 1):
    cal -= cal * (per / 100)
    
    if cal < 1200:
        print(f"Day {day}: {cal:.2f} calories (Diet stabilized below 1200 calories)")
        break
    else:
        print(f"Day {day}: {cal:.2f} calories")
