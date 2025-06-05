
#Write a Python program to calculate the sum of three given numbers:
#If all three values are equal, then return a number equal to 3 times their sum.
#If two values are equal, then return twice their sum.
#If none are equal, just display the sum

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a==b==c:
    print ((a+b+c)*3)
elif a==b or b==c or c==a:
    print ((a+b+c)*2)
else:
    print(a+b+c)