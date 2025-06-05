# Write a Python program to reverse a string.
def perfect(num):
    if num <= 1:
        return False
    
    d = 0
    for i in range(1, num):
        if num % i == 0:
            d += i
    
    return d == num
n = int(input("Enter a number: "))
if perfect(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")