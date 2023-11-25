_str = "Vol State - 447"
print(f"The total number of characters is: {len(_str)}")

# uses "ch" as the function parameter so that when it is called we can pass in "_str" as an argument.
def count_str(ch):
    alpha = 0
    digit = 0       # All these initialize the counts
    space = 0
    lower = 0
    upper = 0
    other = 0
    for ch in _str:     # This loops through the string in "_str".
        if ch.isalpha():
            alpha = alpha + 1

# These "_ = _ + 1" lines relate to the .is___() and will add 1 to the count if the method is found in the string.

            if ch.islower():
                lower = lower + 1

            else:
                upper = upper + 1  # if the Character is alpha but not lower it must be upper.

        elif ch.isdigit():
            digit = digit + 1

        elif ch.isspace():
            space = space + 1

        else:               # if the character is not any of the above methods it must be "Other".
            other = other + 1

    print(f"Alphabetical: {alpha}")     # I was stuck for a bit because of a simple mistake with the print function
    print(f"Digits: {digit}")   # I had the print function inside the if statement that caused the count to repeat
    print(f"Spaces: {space}")   # 1,2,3...8 but then I saw that the print statement had to be outside the if statement
    print(f"Lowercase: {lower}")  # for it to only print the total.
    print(f"Uppercase: {upper}")
    print(f"Other: {other}")


count_str(_str)  # Calls the "count_str" function with and argument of "_str".
