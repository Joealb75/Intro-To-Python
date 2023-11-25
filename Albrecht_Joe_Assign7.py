min_num = int(input("Enter the value for the minimum number: "))
max_num = int(input("Enter the value for the maximum number: "))

total = 0.00  # initializes total for program
count = 0  # initializes count for program

# While True = Do everything in this loop until the user enters "quit" in the "ask" function, once that happens the loop
# will break and the average will be calculated and printed out along with the sum.

while True:
    ask = input(f"Enter a number between {min_num} and {max_num} to add: ")

    if ask.lower() == "quit":
        break

    # .isdigit is a bool expression that checks to see if the input is a number, if so it returns true
    # and this if statement will run.

    if ask.isdigit():

        # takes "ask" and converts it to an int and places it in a new function that can be called as int by default.
        # Didn't have to do it, could have used "int(ask)" in the same places as "num_ask"

        num_ask = int(ask)

        # this if statement checks to see if users input is between the min & max they set, if not they get an error.

        if num_ask < min_num or num_ask > max_num:
            print("ERROR: Invalid Number")

        # if all the above check-out the number the users entered will be added to "total" and the "count" will increase
        # by 1, then the loop could run again.

        else:
            total += num_ask
            count += 1

# These 3 lines are put outside the loop, so they will execute last.

average = total / count
print(f"Sum of all valid numbers you entered is: {total}")
print(f"Average of all valid numbers you entered is: {average}")
