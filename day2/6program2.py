
#In this game of roulette, accept a bet from the user as input and calculate if it is
#■ red or black
#high (3rd 12), low (1st 12) or medium (2nd 12).
#Print an error message if the user provides an input that is out of range.
#Look at the provided image for clues.

red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
def check_bet(bet):
    if bet < 0 or bet > 36:
        return "Error: Please enter a number between 0 and 36."
    if bet == 0:
        return "The number is green (0), it is neither red nor black."
    elif bet in red_numbers:
        color = "Red"
    elif bet in black_numbers:
        color = "Black"
    if 1 <= bet <= 12:
        category = "Low (1st 12)"
    elif 13 <= bet <= 24:
        category = "Medium (2nd 12)"
    else:
        category = "High (3rd 12)"
    
    return f"The number {bet} is {color} and falls in the category: {category}"
bet = int(input("Enter your bet (between 0 and 36): "))
print(check_bet(bet))