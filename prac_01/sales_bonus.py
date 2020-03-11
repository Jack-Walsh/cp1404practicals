"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BENCHMARK = 1000

sales = float(input("Enter sales: $"))
if sales < BENCHMARK:
    print(sales * 1.1)
elif sales >= BENCHMARK:
    print(sales * 1.15)