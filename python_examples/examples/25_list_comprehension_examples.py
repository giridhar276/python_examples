"""
Program 25:
List comprehension examples.
"""

numbers = [1, 2, 3, 4, 5, 6]

# Traditional way
squares = []
for n in numbers:
    squares.append(n * n)

print("Squares using normal loop:", squares)

# List comprehension
squares_comp = [n * n for n in numbers]
print("Squares using comprehension:", squares_comp)

# List comprehension with condition
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# Convert words to uppercase
words = ["python", "data", "ai"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)
