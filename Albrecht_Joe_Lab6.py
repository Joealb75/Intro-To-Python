numbers = range(1, 31, 3)

for numbers in numbers:
    print(numbers)

# numbers was assigned the range function with (1(Starting point), 31(Ending Point), 3(Skip Value) to make the for loop
# cleaner, and if the values needed to be changed in the future you can change it in one place.

keep_going = "Y"

while keep_going == "Y":
    print("Hello There...")
    keep_going = (input("Would you like to keep playing? ")).upper()
    if keep_going == "N":
        print("Thanks for playing!")

    # Not much to explain here, while loop keeps it going until you enter "n". ".upper" is added to avoid user error.
