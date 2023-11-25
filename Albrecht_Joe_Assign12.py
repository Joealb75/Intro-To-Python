mylist = ["these", "are", "random", "words"]
words = []

shortest = mylist[0]
longest = mylist[0]
total_count = 0
avg_count = 0
average = 0

file_name = input("Enter the name of the file: ")  # Asks user for file name to be used throughout the program
file_write = open(file_name, "w")   # Creates file and sets the parameter to "write"

for word in mylist:
    file_write.write(word + '\n')   # Writes words to new file

file_write.close()      # Closes file

print(f"UPDATE: Words have been written to {file_name}.txt")

file_read = open(file_name, "r")    # Opens file and sets the parameter to "read"

for word in file_read:      # Adds each word to empty list
    words.append(word.strip())

for word in words:
    total_count += len(word)    # Counts # of characters in all words
    avg_count += 1              # Used to count # of Words
    if len(word) < len(shortest):   # Finds the shortest word
        shortest = word
    if len(word) > len(longest):    # Finds the longest word
        longest = word

file_read.close()        # Closes file
average = total_count / avg_count   # Gets average

SHORT = f"The shortest word is: {shortest}"
LONG = f"The longest word is: {longest}"                    # Makes it easier to write the output to new file
TOTAL = f"The total amount of characters is: {total_count}"
NUM_WORDS = f"There are {avg_count} words in {file_name}.txt "
AVG = f"The average amount of characters is: {average}"

ALL = [SHORT, LONG, TOTAL, NUM_WORDS, AVG]

print("\n", SHORT, "\n", LONG, "\n", TOTAL, "\n", NUM_WORDS, "\n", AVG)
print()     # Used to help with output formatting

ask = input("Would you like to save these results to a new file?: Enter Y or N: ").upper()

if ask == "Y":
    NF_Name = input("Please enter the file name: ")
    f_write = open(NF_Name, "w")    # Creates file and sets the parameter to "write"
    print()     # Used to help with output formatting
    for var in ALL:
        f_write.write(var + '\n')   # Writes the data to new file
    print(f"UPDATE: The result has been saved in {NF_Name}.txt")
    f_write.close()      # Closes file
