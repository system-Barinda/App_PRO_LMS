# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 1: Create a new file
# 1. Create students.txt using mode "x".
# 2. Write the three student records, placing each student on a separate line.
# Question: What happens if you run the creation code again while students.txt already exists?
# Answer: Running open("students.txt", "x") again raises a FileExistsError because mode "x" (exclusive creation) fails if the file already exists.

import os

# Clean up first if running standalone multiple times during testing
if os.path.exists("students.txt"):
    os.remove("students.txt")

with open("students.txt", "x") as file:
    file.write("101, Alice, IT\n")
    file.write("102, Eric, Electronics\n")
    file.write("103, Diane, IT\n")

print("students.txt created successfully with 3 records.")

# Demonstrating what happens if run again:
try:
    with open("students.txt", "x") as file:
        file.write("Duplicate attempt\n")
except FileExistsError as e:
    print(f"Observation when running creation code again: {type(e).__name__} - {e}")
