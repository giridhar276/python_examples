"""
Program 14:
File read methods:
- read()
- readline()
- readlines()
"""

file_path = "../data/sample.txt"

# read() reads complete file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("Using read():")
    print(content)

# readline() reads one line at a time
with open(file_path, "r", encoding="utf-8") as file:
    print("Using readline():")
    print(file.readline())
    print(file.readline())

# readlines() reads all lines into a list
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Using readlines():")
    print(lines)
