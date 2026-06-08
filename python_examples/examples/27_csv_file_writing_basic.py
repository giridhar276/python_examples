"""
Program 27:
Writing CSV file using built-in csv module.
"""

import csv

students = [
    ["roll_no", "name", "marks"],
    [1, "Amit", 85],
    [2, "Priya", 92],
    [3, "Ravi", 76]
]

with open("../output/new_students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
