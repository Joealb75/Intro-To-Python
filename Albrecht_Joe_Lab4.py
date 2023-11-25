
Power = int(input("How much power do you have?: "))

Max_Power = 350
Min_Power = 10

# Here the code says if you entered a power between 10 and 350 then it is the correct amount.
if Power >= Min_Power and Power <= Max_Power:
    print("Correct Amount: You gave", Power, "power to your character")

# Here the code says if your power is less than 10 or higher than 350 it is incorrect.
if Power < Min_Power or Power > Max_Power:
    print("Incorrect Amount: Go back and practice more")

# I am getting a notification for a problem with the code however it will still run, it says
# "Simplify Chained Comparison" for line 8 - What does this mean?
