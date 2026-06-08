"""
Program 09:
One example covering:
- Objects
- Methods
- Slicing
- Conditions
- Loops
"""

student_name = "  giridhar sripathi  "
marks = [85, 90, 78, 92, 88]
subjects = ("Python", "SQL", "ML", "AI", "Pandas")
profile = {
    "name": student_name.strip().title(),
    "city": "Hyderabad",
    "course": "Data Science"
}
unique_marks = set(marks)

print("Clean name:", profile["name"])
print("First 3 subjects:", subjects[:3])
print("Last 2 marks:", marks[-2:])
print("Unique marks:", unique_marks)

average = sum(marks) / len(marks)

if average >= 80:
    print("Result: Excellent")
else:
    print("Result: Needs improvement")

for subject, mark in zip(subjects, marks):
    print(subject, ":", mark)
