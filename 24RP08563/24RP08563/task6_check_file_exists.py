# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 6: Check whether a file exists
# 1. Ask the user to enter a filename.
# 2. Check whether it exists.
# 3. Display "File found" if it exists; otherwise display "File not found".
# Test with: students.txt and missing.txt.

from pathlib import Path

filename = input("Enter filename: ")
path = Path(filename)

if path.exists() and path.is_file():
    print("File found")
else:
    print("File not found")
