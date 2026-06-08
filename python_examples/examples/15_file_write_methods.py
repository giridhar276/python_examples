"""
Program 15:
File write methods:
- write()
- writelines()
"""

# write() example
with open("../output/write_example.txt", "w", encoding="utf-8") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

# writelines() example
lines = [
    "Python file handling\n",
    "Writing multiple lines\n",
    "Using writelines method\n"
]

with open("../output/writelines_example.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("Files written successfully in output folder.")
