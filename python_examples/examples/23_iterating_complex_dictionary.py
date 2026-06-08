"""
Program 23:
Iterating complex nested dictionary.
"""

company = {
    "department": "IT",
    "employees": {
        "E101": {
            "name": "Amit",
            "skills": ["Python", "SQL", "Excel"],
            "salary": 75000
        },
        "E102": {
            "name": "Priya",
            "skills": ["Java", "Spring", "SQL"],
            "salary": 85000
        },
        "E103": {
            "name": "Rahul",
            "skills": ["Python", "ML", "Pandas"],
            "salary": 95000
        }
    }
}

for emp_id, details in company["employees"].items():
    print("Employee ID:", emp_id)
    print("Name:", details["name"])
    print("Salary:", details["salary"])
    print("Skills:")

    for skill in details["skills"]:
        print("-", skill)

    print("-" * 30)
