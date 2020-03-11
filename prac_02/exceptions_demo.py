try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
When will a ValueError occur?
    When something other than an integer is entered
    
When will a ZeroDivisionError occur?
    When zero is entered as the denominator
    
Could you change the code to avoid the possibility of a ZeroDivisionError?
    You cannot divide by zero; however, you can use a while or if to control the line that will crash
"""

