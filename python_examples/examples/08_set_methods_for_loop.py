"""
Program 08:
Set methods and for loop.
"""

skills = {"Python", "SQL", "Excel"}

# Set methods
skills.add("Power BI")
skills.update(["Machine Learning", "Python"])  # Duplicate Python will not be added

print("Skills:", skills)

# Remove item safely
skills.discard("Excel")

print("After discard:", skills)

# Set operations
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

print("Union:", frontend.union(backend))
print("Intersection:", frontend.intersection(backend))
print("Difference:", frontend.difference(backend))

# For loop
for skill in skills:
    print("Skill:", skill)
