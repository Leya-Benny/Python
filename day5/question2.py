#Color Mixer
RED = "red"
BLUE = "blue"
YELLOW = "yellow"
def main():
    colour1 = input("Enter the first primary colour (red, blue, yellow): ").lower()
    colour2 = input("Enter the second primary colour (red, blue, yellow): ").lower()
    if colour1 not in [RED, BLUE, YELLOW]:
        print("Error: Invalid Colour1.")
    elif colour2 not in [RED, BLUE, YELLOW]:
        print("Error: Invalid Colour2.")
    elif colour1 == colour2:
        print("Error: The two colours you entered are the same.")
    else:
        if colour1==RED:
            if colour2==BLUE:
                print("The mix of RED and BLUE gives PURPLE.")
            elif colour2 == YELLOW:
                print("The mix of RED and YELLOW gives ORANGE.")
        elif colour1 == BLUE:
            if colour2 == RED:
                print("The mix of BLUE and RED gives PURPLE.")
            elif colour2 == YELLOW:
                print("The mix of BLUE and YELLOW gives GREEN.")
        elif colour1 == YELLOW:
            if colour2 == RED:
                print("The mix of YELLOW and RED gives ORANGE.")
            elif colour2 == BLUE:
                print("The mix of YELLOW and BLUE gives GREEN.")
if __name__ == "__main__":
  main()
