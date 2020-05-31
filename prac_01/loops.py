for i in range(1, 22, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("Stars: "))
print(number * "*")

number = int(input("Stars: "))
for i in range(2, number, 2):
    print("*" * i)
