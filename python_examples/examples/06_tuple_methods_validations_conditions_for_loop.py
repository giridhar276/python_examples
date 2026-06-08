"""
Program 06:
Tuple methods, validations, conditions, and for loop.
"""

colors = ("red", "blue", "green", "blue")

print("Tuple:", colors)

# Tuple methods
print("Count of blue:", colors.count("blue"))
print("Index of green:", colors.index("green"))

# Validation
if "red" in colors:
    print("Red is present")

# Condition
if len(colors) >= 3:
    print("Tuple has 3 or more items")

# For loop
for color in colors:
    print("Color:", color)

# Tuple unpacking
first, second, third, fourth = colors
print("First color:", first)
print("Second color:", second)
