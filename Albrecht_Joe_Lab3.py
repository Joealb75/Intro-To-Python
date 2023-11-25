# Here the users input is assigned to pay_rate and set to be a float

pay_rate = float(input("Enter your hourly pay rate: "))

# Here the users input is assigned to hours_worked and set to be a float

hours_worked = float(input("Enter the number of hours you worked last week: "))

# Here hours_worked is multiplied by pay_rate and assigned to pay_check

pay_check = hours_worked * pay_rate

# Here the format function is used to show 2 decimal points (__.00) at the end of the output from pay_check

print("you earned", format(pay_check, '.2f'), "last week")
