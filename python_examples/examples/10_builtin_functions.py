"""
Program 10:
Common built-in functions in Python.
"""

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted:", sorted(numbers, reverse=True))

# type() returns the data type
print("Type:", type(numbers))

# range() generates sequence of numbers
print("Range values:")
for i in range(1, 6):
    print(i)

# enumerate() gives index and value
for index, value in enumerate(numbers):
    print("Index:", index, "Value:", value)

# zip() combines multiple sequences
names = ["Amit", "Priya", "Ravi"]
scores = [85, 92, 76]

for name, score in zip(names, scores):
    print(name, "scored", score)
