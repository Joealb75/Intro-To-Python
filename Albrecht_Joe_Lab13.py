new_games = ["\nMinecraft", "GTA5", "Read Dead Redemption 2"]
file_name = "mygames.txt"


def add_games(file_name, game_list):        # Creates Function
    try:        # Try to open the file to see if it exists
        file = open(file_name, "r")
        file_exists = True      # Indicates the file exists
        file.close()
    except FileNotFoundError:
        return False        # If the file is not found return false

    try:    # Try to open the file in append mode to add games
        file = open(file_name, "a")
        for game in game_list:      # Loop through the new games list and write each game to the file
            file.write(game + "\n")
        file.close()
        return True     # Successfully appended to file
    except:
        return False    # Return False if any error occurs during appending


Result = add_games(file_name, new_games)    # Calls the function and stores it in "Result"

if Result is True:
    file_open = open(file_name, 'r')
    print("These are the video games:")
    for line in file_open:      # Loops through the file and prints every game in it
        print(line.strip())
    file_open.close()
else:
    print("Video games were not added to the file.")    # Print if games were not added
