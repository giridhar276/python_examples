"""
Program 28:
JSON read and write examples using built-in json module.
"""

import json

employee = {
    "id": 101,
    "name": "Anita",
    "department": "IT",
    "skills": ["Python", "SQL", "Power BI"]
}

# Write dictionary to JSON file
with open("../output/employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

print("JSON file written successfully.")

# Read JSON file
with open("../output/employee.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Employee name:", data["name"])
print("Skills:", data["skills"])
