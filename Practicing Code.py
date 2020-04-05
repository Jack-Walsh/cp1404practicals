"""
# jumps through every second letter
hellostring = "hello world"
print(hellostring [::2])


# prints how many characters i ask for
hellostring = "hello world"
print(hellostring [:4])

# the range i tell it too print
hellostring = "hello world"
print(hellostring [3:-2])

# skip an amount of characters and show the rest
hellostring = "hello world"
print(hellostring [2:])

for i in range(1, 10, 4):
    print(i, i * 2, end=" ")

x = 10
while x > 4:
    print(x, end=" ")
    x = x - 2


def main():

    age = 0
    valid_age = False
    while not valid_age:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be >=0")
            else:
                valid_age = True
        except ValueError:
            print("Invalid, please enter number")

    if is_even(age):
        print("{} is even".format(age))
    else:
        print("{} is odd".format(age))

def is_even(number):
    if number % 2 == 0:
        return True
    # else:
      #  return False

main()

def test_is_even():
    for i in range(5):
        print("{} is {}".format(i, is_even(i)))

# test_is_even()

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False

print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))
"""
