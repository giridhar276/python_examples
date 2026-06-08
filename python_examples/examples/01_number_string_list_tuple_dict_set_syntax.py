"""
Program 01:
Basic syntax of Python objects:
- Number
- String
- List
- Tuple
- Dictionary
- Set
"""

# Number examples
age = 30              # integer
price = 99.50         # float
complex_number = 2 + 3j

print("Integer:", age)
print("Float:", price)
print("Complex:", complex_number)

# String example
name = "Python"
print("String:", name)

# List example
# List is ordered, mutable, and allows duplicate values.
fruits = ["apple", "banana", "mango", "apple"]
print("List:", fruits)

# Tuple example
# Tuple is ordered, immutable, and allows duplicate values.
coordinates = (10, 20, 30)
print("Tuple:", coordinates)

# Dictionary example
# Dictionary stores data in key-value format.
student = {
    "name": "Ravi",
    "age": 21,
    "course": "Python"
}
print("Dictionary:", student)

# Set example
# Set is unordered and stores unique values.
unique_numbers = {10, 20, 30, 10, 20}
print("Set:", unique_numbers)
