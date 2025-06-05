def takeInput():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")
    return n1, n2, op

def displayResult(n1, n2, op):
    if op == '+':
        r = n1 + n2
        print(f"{n1} + {n2} = {r}")
    elif op == '-':
        r = n1 - n2
        print(f"{n1} - {n2} = {r}")
    elif op == '*':
        r = n1 * n2
        print(f"{n1} * {n2} = {r}")
    elif op == '/':
        if n2 != 0:
            r = n1 / n2
            print(f"{n1} / {n2} = {r}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operator! Please use +, -, *, or /.")

n1, n2, op = takeInput()
displayResult(n1, n2, op)