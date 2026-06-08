"""
Program 30:
Mini project using:
- List
- Dictionary
- Function
- Condition
- Loop
- File writing
"""

students = [
    {"name": "Amit", "marks": [80, 75, 90]},
    {"name": "Priya", "marks": [95, 88, 92]},
    {"name": "Ravi", "marks": [60, 65, 70]},
    {"name": "Neha", "marks": [85, 82, 89]}
]

def calculate_average(marks):
    """Calculate average marks."""
    return sum(marks) / len(marks)

def get_grade(average):
    """Return grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"

report_lines = []

for student in students:
    average = calculate_average(student["marks"])
    grade = get_grade(average)

    line = f"{student['name']} | Average: {average:.2f} | Grade: {grade}"
    print(line)
    report_lines.append(line + "\n")

# Save report into file
with open("../output/student_report.txt", "w", encoding="utf-8") as file:
    file.writelines(report_lines)

print("Student report generated in output folder.")
