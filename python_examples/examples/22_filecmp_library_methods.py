"""
Program 22:
Built-in library: filecmp module methods.
"""

import filecmp

file_a = "../data/compare_a.txt"
file_b = "../data/compare_b.txt"
file_c = "../data/compare_c.txt"

# Compare two files
print("compare_a and compare_b are same:", filecmp.cmp(file_a, file_b))
print("compare_a and compare_c are same:", filecmp.cmp(file_a, file_c))

# Shallow=False compares actual file content
print("Deep comparison:", filecmp.cmp(file_a, file_c, shallow=False))
