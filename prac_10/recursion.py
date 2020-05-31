"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# 2 - Answer was 3
print("do_it function answer: {}".format(do_it(5)))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring