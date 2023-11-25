
products_sold = int(input("How many total products did you sell last week? "))
total = 0.0
# Here "days" is the iteration, so starting at 1 and will count up depending on the amount of products sold.

for days in range(1, products_sold + 1):
    price = int(input(f"What is the total price of the product sold on day {days}: "))
    total += price  # This line takes the users input of price and adds it to a running total
    print("")

avg_price = total / products_sold   # This calculates the average and puts it into avg_price
print(f"Total amount sold is ${total}")
print(f"Average price per day is ${avg_price}")
