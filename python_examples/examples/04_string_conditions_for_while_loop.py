"""
Program 04:
String conditions, for loop, and while loop.
"""

password = "Python@123"

# String condition validations
if len(password) >= 8:
    print("Password has enough characters")
else:
    print("Password is too short")

if password.isalnum():
    print("Password has only alphabets and numbers")
else:
    print("Password has special characters also")

# For loop with string
name = "Python"

print("Characters using for loop:")
for char in name:
    print(char)

# While loop with string index
index = 0

print("Characters using while loop:")
while index < len(name):
    print(name[index])
    index += 1
