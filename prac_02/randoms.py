import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1. What did you see on line 1?
    Line 1 was randomly selecting every number between 5 and 20
2. What was the smallest number you could have seen, what was the largest?
    Smallest Number on Line 1: 5
    Largest Number on Line 1: 20

3. What did you see on line 2?
    Line 2 was randomly selecting every odd number between 3 and 10
4. What was the smallest number you could have seen, what was the largest?
    Smallest Number: 3
5. Could line 2 have produced a 4?
    No

6. What did you see on line 3?
    Line 3 was randomly selecting every number between 2.5 and 5.5 giving a random floating point.
7. What was the smallest number you could have seen, what was the largest?
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

