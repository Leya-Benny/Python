#Currency Converter
RATE = {"Canada": 1.56,"USA": 1.09, "Cambodia": 4650, "United Kingdom": 0.87 }

SALARY = {"Canada": 56000,"USA": 45000,"Cambodia": 7649856,"United Kingdom": 45423}

def convertSalary(sal, co):
    if co in RATE:
        return sal * RATE[co]
    return None

def main():
    sal = float(input("Please enter your salary: "))
    co = input("Enter the country you want to migrate to: ").capitalize()

    if co not in RATE:
        print("Invalid country.")
        return
    
    convert = convertSalary(sal, co)
    
    if convert < SALARY[co]:
        print(f"You will be poor in {co} with a salary of {convert:.2f} {co}.")
    else:
        print(f"You will be rich in {co} with a salary of {convert:.2f} {co}.")

if __name__ == "__main__":
    main()
