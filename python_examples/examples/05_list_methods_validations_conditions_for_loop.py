"""
Program 05:
List methods, validations, conditions, and for loop.
"""

students = ["Amit", "Priya", "Ravi"]

# List methods
students.append("Neha")          # Add item at end
students.insert(1, "Sara")       # Insert at specific index
students.remove("Ravi")          # Remove specific value

print("Students:", students)

# Validation
if "Priya" in students:
    print("Priya is available in the list")

# Condition
if len(students) > 3:
    print("More than 3 students are available")

# For loop
for student in students:
    print("Student name:", student)

# Sorting
students.sort()
print("Sorted students:", students)

# Reverse
students.reverse()
print("Reversed students:", students)
