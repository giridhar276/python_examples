"""
Program 03:
String methods and slicing examples.
"""

message = "  welcome to Python Programming  "

print("Original:", message)

# String methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title case:", message.title())
print("Strip spaces:", message.strip())
print("Replace:", message.replace("Python", "Java"))
print("Count of o:", message.count("o"))
print("Starts with spaces:", message.startswith("  "))
print("Ends with spaces:", message.endswith("  "))

# Slicing examples
text = "PYTHON"

print("First character:", text[0])
print("Last character:", text[-1])
print("First 3 characters:", text[0:3])
print("From index 2:", text[2:])
print("Till index 4:", text[:4])
print("Reverse string:", text[::-1])
print("Every second character:", text[::2])
