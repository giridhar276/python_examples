"""
Program 12:
Lambda functions.
"""

# Normal function
def square_normal(n):
    return n * n

print("Normal function square:", square_normal(5))

# Lambda function
square_lambda = lambda n: n * n

print("Lambda square:", square_lambda(5))

# Lambda with two arguments
add = lambda a, b: a + b

print("Addition using lambda:", add(10, 20))

# Lambda with condition
check_even = lambda n: "Even" if n % 2 == 0 else "Odd"

print("Number type:", check_even(11))
