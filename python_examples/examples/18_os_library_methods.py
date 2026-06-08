"""
Program 18:
Built-in library: os module methods.
"""

import os

print("Current working directory:", os.getcwd())

# List files and folders in current directory
print("Files/Folders:", os.listdir("."))

# Create folder if it does not exist
folder_name = "../output/os_demo_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)

# Join paths safely
file_path = os.path.join(folder_name, "demo.txt")
print("Joined path:", file_path)

# Write a file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Created using os module example.")

# Check if file exists
print("File exists:", os.path.isfile(file_path))
print("Folder exists:", os.path.isdir(folder_name))
