# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 1: Create a new file using mode "x"
# Question: What happens if you run the creation code again while students.txt already exists?
# Answer: It raises a FileExistsError because mode "x" only creates a file if it does not already exist.

import os

# Remove students.txt first if testing multiple times
if os.path.exists("students.txt"):
    os.remove("students.txt")

# Create students.txt and write 3 records using writelines()
records = [
    "101, Alice, IT\n",
    "102, Eric, Electronics\n",
    "103, Diane, IT\n"
]

with open("students.txt", "x") as student_file:
    student_file.writelines(records)

print("Done: students.txt has been created.")

# Show what happens when running mode "x" again
try:
    with open("students.txt", "x") as student_file:
        student_file.write("104, Test, IT\n")
except FileExistsError:
    print("Error observed: students.txt already exists (FileExistsError).")
