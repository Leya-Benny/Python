my_numbers = [4, 6, 9, 12, 17, 22, 27, 33, 44]
print("Original list:")
for n in my_numbers:
    print(n, end=" ")
for i in range(len(my_numbers) - 1):
    index = i
    for j in range(i + 1, len(my_numbers)):
        if my_numbers[j] > my_numbers[index]:
            index = j
    my_numbers[i], my_numbers[index] = my_numbers[index], my_numbers[i]
print("\nSorted list:")
for num in my_numbers:
    print(num, end=" ")
