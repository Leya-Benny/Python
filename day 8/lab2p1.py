#Average Temperature Over Years
m = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
years = int(input("Enter the number of years: "))
ttemp = 0 
tmonth = 0  
y = 1
while y <= years:
    yearTotal = 0
    print(f"\nYear {y}:")
    month = 0
    while month < 12:
        t = float(input(f"Enter the temperature for {m[month]}: "))
        yearTotal += t
        ttemp += t
        tmonth += 1
        month += 1
    Yavg = yearTotal / 12
    print(f"\nAverage high temperature for Year {y}: {Yavg:.2f}")
    y += 1
Oavg = ttemp / tmonth
print(f"Overall average high temperature over {tmonth} months: {Oavg:.2f}")

