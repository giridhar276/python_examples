"""
Program 24:
Basic exception handling.
"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Please enter only numeric value.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program completed.")
