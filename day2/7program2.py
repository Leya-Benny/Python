#Accept the score of a student as input and calculate the grade.
#Use a combination of boundary inclusive and boundary exclusive operators. (To be submitted)
# 100
# Perfect
# 90-99
# A
# 80-89
# B
# 70-79
# C
# 60-69
# D
# <60
# F

n=int(input('enter a number: '))
if n==100:
    print('perfect')
elif n>=90 and n<=99:
    print('A')
elif n>=80 and n<=89:
    print('B')
elif n>=70 and n<=79:
    print('C')
elif n>=60 and n<=69:
    print('D')
else:
    print('F')