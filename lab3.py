# This is Ryan Lim and Cesar lab

import random


def loan_qualifier():
    """
    :return: evaluate conditions and print the correct sentence.
    """
    print("running loan qualifier")
    annual_income = float(input("enter your monthly salary:")) * 12
    how_long = int(input("enter the number of years employed:"))
    if annual_income >= 50000 and how_long >= 3:
        print("you qualify for a loan")
    if annual_income <= 50000 and how_long<= 3:
        print("your income must be 50000 or more, and you must be employed for 3 years or more")
    elif annual_income < 50000:
        print("your income must be 50000 or more, you don't qualify for a loan")
    elif how_long < 3:
        print("you must be employed for 3 years or more, you don't qualify for a loan")


def is_magic_date():
    """
    :User inputs month,day,year values
    :if month*day= year true, print magic date,
    :if false, print not magic date.
    """
    print("running is magic date")
    month_value = int(input("input month value:"))
    if month_value < 1 or month_value > 12:
        print("invalid month value")
        return
    day_value = int(input("input day value:"))
    if day_value < 1 or day_value > 31:
        print("the day value must be between 1 and 31 inclusive")
        return
    year_value = int(input("input two digit year value:"))
    if year_value < 10:
        print("the year value must be positive and it must be two digit")
        return
    elif month_value * day_value == year_value:
        print("the date %d - %d - %d is a magic date" % (month_value, day_value, year_value))
    else:
        print("the date %d - %d - %d is not a magic date" % (month_value, day_value, year_value))


def play_chicago():
    """
    :If random number + random number = count, user get 1 point
    :When user say "yes" when asked, function loop until it reaches round 13.
    :When game is over, it prints, ending message with prize won.
    """
    print("running playing chicago")
    count = 2
    win = 0
    while count < 13:
        dice1 = random.randint(1, 6)   #import random module
        dice2 = random.randint(1, 6)   #import random module
        if dice1 + dice2 == count:
            print("round number", count)
            print("first dice number is", dice1)
            print("second dice number is", dice2)
            print("you won a point, your current points are", win + 1)
            if count == 12:
                print("the game is over you earned", win)
                return
            vote = str(input('do you want to play again?, enter "yes" to continue'))
            count = count + 1
            win = win + 1
            if vote == str("yes"):
                continue
            else:
                print("the game is over you earned", win)
                return

        else:
            print("round number", count)
            print("first dice number is", dice1)
            print("second dice number is", dice2)
            print("no point, your current points are", win)
            if count == 12:
                print("the game is over you earned", win)
                return
            vote = str(input('do you want to play again?, enter "yes" to continue'))
            count = count + 1
            if vote == str("yes"):
                continue
            else:
                print("the game is over you earned", win)
                return
    print("the game is over you earned", win)


def is_even(number):
    """
    :param number:User input number between 1-36
    :return: if number is even, it returns True, if odd, it returns False.
    """
    if number % 2 == 0:
        number = True
    else:
        number = False
    return number


def get_pocket_colour(number):
    """
    :param number: user input numbers: pocket number between 0-36
    :return: after evaluate, it will say which color.
    """
    number1_10 = 0
    number10_18 = 10
    number18_28 = 18
    number28_36 = 28
    green = [0]
    black = []   #this list will be filled as the number go through the functions below
    red = []    #this list will be filled as the number go through the functions below
    while number1_10 < 10:  #evaluate number 1-10
        number1_10 += 1
        if number1_10 % 2 == 0:
            black.append(number1_10)
        else:
            red.append(number1_10)
    while number10_18 < 18:   #evaluate number 10-18
        number10_18 += 1
        if number10_18 % 2 == 0:
            red.append(number10_18)
        else:
            black.append(number10_18)
    while number18_28 <28:   #evaluate number 18-28
        number18_28 += 1
        if number18_28 % 2 == 0:
            black.append(number18_28)
        else:
            red.append(number18_28)
    while number28_36 < 36:  #evaluate number 28-36
        number28_36 += 1
        if number28_36 % 2 ==0:
            red.append(number28_36)
        else:
            black.append(number28_36)
    if number in black:
        return "black"
    elif number in red:
        return "red"
    elif number in green:
        return "green"

def play_roulette():
    """
    :Collect user data, run functions is_even and get_pocket_colour, and print according to the conditions.
    """
    print("running play roulette")
    while True:
        pocket_number = int(input("enter a pocket number between 0 to 36 inclusive:"))
        bet_amount = int(input("enter your bet amount:"))
        even_or_odd = is_even(pocket_number)
        color = get_pocket_colour(pocket_number)
        if color == "green":
            print("you neither win nor lose you have", bet_amount)
        if even_or_odd is True and color == "black":
            win = bet_amount * 1.5
            print("you won you have", win)
        if even_or_odd is True and color == "red":
            win = bet_amount * 2
            print("you won you have", win)
        if even_or_odd is False and color == "black":
            win = bet_amount
            print("you lose you have", win)
        if even_or_odd is False and color == "red":
            win = bet_amount * 1.5
            print("you won you have", win)
        if pocket_number < 0 or pocket_number > 36:
            print("Error!, You have entered a number that is outside the range of 0 through 36")
        yes_or_no = str(input('type "yes" to continue, anything else to stop'))
        if yes_or_no == "yes":
            continue
        else:
            break


def main():
    """
    :Calling functions 
    """
    loan_qualifier()
    is_magic_date()
    play_chicago()
    play_roulette()


if __name__ == '__main__':
    main()
