
numbers = []
for i in range(5):
    get_number = int(input("Number: "))
    numbers.append(get_number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The sum of all numbers is", sum(numbers))
print("The average of the number is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

get_username = input("Please enter your username")
if get_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")