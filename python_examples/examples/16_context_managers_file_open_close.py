"""
Program 16:
Context manager with file open and close.

The 'with' statement automatically closes the file.
"""

file_path = "../data/sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# No need to manually call file.close()
print("File automatically closed after with block.")
