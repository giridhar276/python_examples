"""
Program 07:
Dictionary methods, validations, and for loop.
"""

employee = {
    "id": 101,
    "name": "Anita",
    "department": "IT",
    "salary": 75000
}

print("Employee:", employee)

# Dictionary methods
print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())

# get() method avoids error if key is missing
print("Employee city:", employee.get("city", "City not available"))

# Add new key-value pair
employee["city"] = "Hyderabad"

# Update value
employee["salary"] = 80000

# Validation
if "department" in employee:
    print("Department key exists")

# For loop over keys
for key in employee:
    print(key, "=", employee[key])

# For loop over key-value pairs
for key, value in employee.items():
    print("Key:", key, "| Value:", value)
