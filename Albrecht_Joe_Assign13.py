file_name = "Students.txt"
student_file = open(file_name, 'r')  # Opens file as "read"

file_line = student_file.readline()     # Read line of file_name
current_student = file_line.split("-")  # Splits the file at "-"
low_student = current_student[0]        # index 0 of current_student list = Students name and assigns to "low_student"
low_score = int(current_student[1])     # index 1 of current_student list = Students grade assigns to "low_score"
                                        # and converts it from a str to an int
num_records = 1  # Sets counter

for current_line in student_file:   # Loops through each line in the file
    try:
        current_student = current_line.split("-")   # Splits the current line into student & score
        current_name = current_student[0]       # Assigns Student name to current name
        current_score = int(current_student[1])  # Changes students score from str to int and assigns to current_score

        if current_score < low_score:   # compares current score & lowest score
            low_score = current_score   # if current score is < low_score it updates
            low_student = current_name  # Adds the corresponding students name

        num_records += 1    # adds 1 to num_record for each valid record

    except ValueError:  # Catches invalid entries in the file and displays the message below
        print("There seems to be a typo in the file you selected: Make sure the file is formatted: EX. Tom-87 ")

student_file.close()    # closes the file

if num_records > 0:
    try:
        print(f"{low_student} had the Lowest Score of {low_score}")  # Prints results of the file
        print(f"Number of records in {file_name}: {num_records}")    # Prints number of records in file

    except IOError:  # Catches any issues with opening the file and displays the message below
        print("The file could not be opened")
