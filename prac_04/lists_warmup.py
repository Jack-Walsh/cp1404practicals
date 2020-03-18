
numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])  # 3
print(numbers[-1])  # 2
print(numbers[3])  # 1
print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # 1
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 5, 9, 2, 6, 5, 3]

# Write Python expressions (in the same Python file) to achieve the following:

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
# 2. Change the last element of numbers to 1
# 3. Get all the elements from numbers except the first two (slice)
# 4. Check if 9 is an element of numbers

numbers[0] = "ten"

numbers[-1] = 1

print(numbers[2:])

print(9 in numbers)
