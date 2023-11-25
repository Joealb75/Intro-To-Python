in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")

# \/ Says while length of user input is < 4 or > 15 or users input contains non-alphabetical characters do the following
while len(in_tag) < 4 or len(in_tag) > 15 or in_tag.isalpha() == False:

    # Checks to see if the users input is less than 4 and is only alphabetical characters.
    if len(in_tag) < 4 and in_tag.isalpha() == True:
        print("Invalid gamer tag! Too few characters!")
        in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")

    # Checks to see if the users input is less than 4 and contains non-alphabetical characters.
    if len(in_tag) < 4 and in_tag.isalpha() == False:
        print("Invalid gamer tag! Too few characters! You cannot have non-alphabetical characters!")
        in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")

    # Checks to see if the users input is greater than 15 and is only alphabetical characters.
    if len(in_tag) > 15 and in_tag.isalpha() == True:
        print("Invalid gamer tag! Too many characters!")
        in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")

    # Checks to see if the users input is less than 4 and contains non-alphabetical characters.
    if len(in_tag) > 15 and in_tag.isalpha() == False:
        print("Invalid gamer tag! Too many characters! You cannot have non-alphabetical characters!")
        in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")

    # Checks to see if the users input is between 4-15 and contains non-alphabetical characters.
    if len(in_tag) in range(4, 15) and in_tag.isalpha() == False:
        print("Invalid gamer tag! You cannot have non-alphabetical characters!")
        in_tag = input("Enter a game name with alphabetical characters and between 4 and 15 characters: ")


if len(in_tag) in range(4, 15) and in_tag.isalpha() == True:
    print(f"Gamer Tag: {in_tag} is Accepted")

# Checks to see if the users input is between 4-15 and contains alphabetical characters.
# This statement has to be outside the while loop so that if the user enters a correct gamer tag the first time
# it will print "Gamer Tag: ___ is Accepted"
