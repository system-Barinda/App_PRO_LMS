# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 2: Open and read a file using mode "r"
# Questions:
# 1. What does "r" allow? It opens the file for reading only.
# 2. Why use with open(...)? It closes the file automatically when done.
# 3. What happens if the file does not exist? Python gives a FileNotFoundError.

# Step 1: Read entire file
print("1. Full file content:")
with open("students.txt", "r") as student_file:
    content = student_file.read()
    print(content)

# Step 2: Read first line only
print("2. First line:")
with open("students.txt", "r") as student_file:
    first_line = student_file.readline()
    print(first_line.strip())

# Step 3: Loop through each record
print("3. All records one by one:")
with open("students.txt", "r") as student_file:
    for row in student_file:
        print("Student ->", row.strip())
