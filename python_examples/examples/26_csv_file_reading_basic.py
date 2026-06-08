"""
Program 26:
Reading CSV file using built-in csv module.
"""

import csv

file_path = "../data/students.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
