"""
Program 11:
User-defined functions.
"""

# Function without parameter
def greet():
    print("Welcome to Python training")

greet()

# Function with parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Addition:", result)

# Function with default parameter
def welcome_user(name="Participant"):
    print("Hello", name)

welcome_user()
welcome_user("Giridhar")

# Function returning multiple values
def calculate(a, b):
    addition = a + b
    multiplication = a * b
    return addition, multiplication

add_result, multiply_result = calculate(5, 4)
print("Addition:", add_result)
print("Multiplication:", multiply_result)
