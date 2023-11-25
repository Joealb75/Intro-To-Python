# Lines 3 & 4 prompts the user to enter the amount of inventory they sold

_5k_or_less = float(input("Enter the total inventory sold of 5000 or below: "))
greater_then_5k = float(input("Enter the total inventory sold more than 5000: "))

# Lines 8 & 9 takes the commission variables and multiples them by their respective rates

standard_commission = _5k_or_less * .10
bonus_commission = greater_then_5k * .15

# Line 13 totals up the commission

total_commission = standard_commission + bonus_commission

# Line 17 creates a new line and formats the total commission to have 2 decimal points

print("\nThe total commission check is $", format(total_commission, '.2f'), sep="")
