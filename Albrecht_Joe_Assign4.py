# Here Play_Again is set to Yes so that the game will loop until the user says "no" then game will end.
# This was done to make it easier to test the code, so I don't have to re-run it every time.
Play_Again = "YES"

# This is a while loop that says while Play_Again == Yes keep re-running this code.
while Play_Again == "YES":
    Player = int(input("Enter the number for your player: "))

    if Player >= 1 and Player <= 63:
        print("\nWelcome to Crossy Bridge")

    elif Player < 1 or Player > 63:
        print("Invalid Player Number, Please choose a number between 1 and 63")

    if Player == 1:
        print("You crossed the Black Bridge")  # For lines 15 - 46 the process remains the same.
#                                               # if the players number falls between the range identified it will
    elif Player >= 2 and Player <= 13:         # then decide if it is an even or an odd number using Player % 2 == 0
        if Player % 2 == 0:                    # if even it crosses a predetermined bridge, if odd it crosses the other
            print("You crossed the Brown Bridge")
        else:
            print("You crossed the Green Bridge")

    elif Player >= 14 and Player <= 24:
        if Player % 2 == 0:
            print("You crossed the Orange Bridge")
        else:
            print("You crossed the Purple Bridge")

    elif Player >= 25 and Player <= 29:
        if Player % 2 == 0:
            print("You crossed the White Bridge")
        else:
            print("You crossed the Red Bridge")

    elif Player >= 30 and Player <= 43:
        if Player % 2 == 0:
            print("You crossed the Pink Bridge")
        else:
            print("You crossed the Blue Bridge")

    elif Player >= 44 and Player <= 63:
        if Player % 2 == 0:
            print("You crossed the Gray Bridge")
        else:
            print("You crossed the Gold Bridge")

# Here the game is asking for the users input to play again, ".upper() was added to make sure it worked with Play_Again.
    Play_Again = input("\nWould you like to play again? | Enter Yes or No: ").upper()

    if Play_Again == "YES":
        print("You started a new round \n")
    else:
        print("Thank you for playing Crossy Bridge!")
