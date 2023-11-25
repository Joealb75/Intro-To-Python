
movie_list = []  # Creates empty list
ask_q = input("Enter the name of a movie, enter -1 to stop: ")


while ask_q != "-1":  # Asks question until user enters "-1" to stop
    movie_list.append(ask_q)  # Adds users input to list
    ask_q = input("Enter the name of a movie, enter -1 to stop: ")

list_len = len(movie_list)
count = 1  # Sets list counter

print("\nThe elements in the list include: ", end="")

for movie in movie_list:  # For every movie in the list do this
    # list_len = len(movie_list)
    if count != list_len:  # if count != to length of the list add 1 to the counter
        count += 1
        print(movie, end=", ")  # print each movie and separate it with a ","
    else:
        print(movie, end="")  # print the last movie with no ","


print(f"\nThe Length of the list is {list_len}")  # prints the number of items in the list

del movie_list[0]  # deletes the first item in the list
print("Deleting index 0...")
# print(f"the Length of the list is {list_len}")

list_len = len(movie_list)
count = 1  # Sets list counter

print("\nThe elements in the list include: ", end="")

for movie in movie_list:  # For every movie in the list do this
    # list_len = len(movie_list)
    if count != list_len:  # if count != to length of the list add 1 to the counter
        count += 1
        print(movie, end=", ")  # print each movie and separate it with a ","
    else:
        print(movie, end="")  # print the last movie with no ","


print(f"\nThe Length of the list is {list_len}")  # prints the number of items in the list

