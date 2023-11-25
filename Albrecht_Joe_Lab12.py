favorite_games = ["CSGO", "Illuvium", "Elden Ring"]  # Creates list of my favorite video game

game_list = []  # Creates empty game list

file = open("mygames.txt", "r")     # Creates "mygames.txt" file and sets the parameter to "read"
for line in file:
    game_list.append(line.strip())  # for every line in file add it to the empty game_list and strip the white space

file.close()    # Closes file

print("My three favorite video games read from a file:")
for game in game_list:  # for every game in the list print the game
    print(game)

file.close()

file = open("videogames.txt", "w")  # Creates "videogames.txt" file and sets the parameter to "write"
game_names = "\nVideo games written to a file:\n"   # adds \n to make the output easily readable

for w_game in range(len(game_list)):
    game_names += game_list[w_game]  # for every game in game_list add it to game_names
    if w_game < len(game_list) - 1:  # if game is less than the length of game_list -1 add a ", "
        game_names += ', '

file.write(game_names)  # Writes the game names to the file with "Video games written to a file:"

file.close()

print(game_names)
