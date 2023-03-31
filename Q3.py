PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

numberOfPennies = int(input("Enter the number of pennies:"))
numberOfNickels =int(input("Enter the number of nickels:"))
numberOfDimes = int(input("Enter the number of dimes:"))
numberofQuaters = int(input("Enter the number of quaters:"))
totalCents = numberOfPennies*PENNY_VALUE + numberOfNickels* NICKEL_VALUE + numberOfDimes * DIME_VALUE + numberofQuaters * QUARTER_VALUE
totalDollars = totalCents / PENNIES_IN_DOLLAR
#morethan or lessthan or else
if totalDollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif totalDollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")