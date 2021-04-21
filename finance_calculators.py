# Importing math module
import math

# Requesting an integer and storing it in a variable called 'number'.
calculation = input("\nChoose either 'investment' or 'bond' from the menu below to proceed:"
                    "\n\n1. investment         - to calculate the amount of interest you'll earn on investment"
                    "\n2. bond             - to calculate the amount you'll have to pay on a home loan     \n\n")


# Using an if, elif, else-statement to determine what should be printed.
# The result will be printed out.
# If the number is not divisible by 2 or 5, then else statement will be executed.

if calculation == 'Bond' or calculation == 'bond' or calculation == 'BOND' or calculation == '1':

    deposit = int(input("\nInsert your deposit amount:  R"))

    interest_rate = int(input("\nInsert your interest rate percentage(%). Only input the number value:   "))
    interest_rate_percentage = interest_rate / 100

    year_span = int(input("\nInsert the number of years you plan on investing for:  "))

    interest = input("\nWhat type of interest would you like to use?"
                     "\n1. Simple"
                     "\n2. Compound\n\n")

    if interest == 'Simple' or interest == 'simple' or interest == 'SIMPLE' or interest == '1':
        total = deposit * (1 + interest_rate_percentage * year_span)
        print(f"\n\nYour interest total is: R{total}.00")

    elif interest == 'Compound' or interest == 'compound' or interest == 'COMPOUND' or interest == '2':
        total = int(deposit * math.pow((1 + interest_rate_percentage), year_span))
        print(f"\n\nYour interest total is: R{total}.00")
    else:
        print(f"\n\nInvalid input")


elif calculation == 'Investment' or calculation == 'investment' or calculation == 'INVESTMENT' or calculation == '2':

    month_num = int(input("\nInsert the number of months planned for bond repayment:    "))

    for x in range(month_num):
        print("Enter credit principal:")
        p = float(input())
        print("Enter your credit interest:")
        i = float(input()) / 100 * (1 / 12)
        a = p * ((i * ((1 + i) ** month_num)) / (((1 + i) ** month_num) - 1))
        print("Your payment = {}!".format(math.ceil(a)))
else:
    print(f"\n\nInvalid input")

# ------------------------------------------------------------------------------------------------------------------- #

# References:

# - HyperionDev (2020). SE L1T11 - Logical Programming - Operators - Task 11. Retrieved 1 February 2021,
#   from Dropbox/ Darren Noortman/ Task 11/ SE L1T11 - Logical Programming - Operators.pdf

# ------------------------------------------------------------------------------------------------------------------- #
