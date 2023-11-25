NUMBERS = [22, 18, 44, 33, 41, -1, 50, 100, 48, 31, 26, 3]

valid_num = []

for num in NUMBERS:  # Checks to see if each number in NUMBERS is between 25 & 50
    if num in range(25, 51):
        valid_num.append(num)  # adds numbers between 25-50 to valid_num list

print(f"Valid Numbers List: {valid_num}")

total = 0
average = 0
count = 0

for num in valid_num:  # Goes through each num in list
    count += 1  # adds 1 to count for each number in list
    total += num
    average = total // count
print(f"Total: {total}")
print(f"Average: {average}")
