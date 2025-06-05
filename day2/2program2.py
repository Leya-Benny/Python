
#Given an integer, n, perform the following conditional actions:
#If n is odd, print "Range A"
#If n is even and within the inclusive range of 2 to 5, print "Range B"
#If n is even and within the inclusive range of 6 to 20, print "Range C"
#If n is even and greater than 20, print "Range D"
n=int(input("Enter the number:"))
if n%2!=0:
    print ("Range A")
elif n%2==0 and n>=2 and n<=5:
    print ("Range B")
elif n%2==0&n>=6&n<=20:
    print ("Range C")
else:
    print ("Range D")