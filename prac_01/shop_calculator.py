"""A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

The output should look something like (bold text represents user input):

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

"""
total_price = 0

num_items = int(input("Number of items: "))

# print amount of item prices as inputted by user
for i in range(1, num_items + 1):
    item_price = float(input("Price of item: "))
    total_price += item_price

# apply discount of 10%
if total_price > 99:
    total_price = total_price * 0.9

# print total
print("Total price for {} items is {}".format(num_items, total_price))
