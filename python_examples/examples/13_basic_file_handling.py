"""
Program 13:
Basic file handling.
"""

# Open a file in read mode
file = open("../data/sample.txt", "r", encoding="utf-8")

# Read entire file content
content = file.read()

print(content)

# Always close the file after usage
file.close()
