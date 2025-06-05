n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            print("#", end="")
        else:
            print(" ", end="")
    print()

