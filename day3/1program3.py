#1. Write a function named right_justify that takes a string named 's' as a parameter and prints the string with enough leading spaces 
#so that the last letter of the string is in column 70 of the display.
# >>> right_justify('monty')
# monty
# Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len that returns the length of a string,
# so the value of len('monty') is 5.

def print_box_grid(rows, cols):
    for i in range(rows):
        print("+" + "-" * 4 + "+" + "-" * 4 + "+")
        for j in range(4):
            print("/" + " " * 4 + "/" + " " * 4 + "/")
    print("+" + "-" * 4 + "+" + "-" * 4 + "+")
print_box_grid(2, 2)
