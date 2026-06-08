"""
Program 17:
Lambda with map() and filter().
"""

numbers = [1, 2, 3, 4, 5, 6]

# map() applies a function to every item
squares = list(map(lambda n: n * n, numbers))
print("Squares:", squares)

# filter() filters items based on condition
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Convert names to uppercase using map
names = ["amit", "priya", "ravi"]
uppercase_names = list(map(lambda name: name.upper(), names))
print("Uppercase names:", uppercase_names)
