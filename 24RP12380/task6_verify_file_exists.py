# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 6: Check whether a file exists
# Test with: students.txt and missing.txt

from pathlib import Path

user_file = input("Enter filename: ")
file_path = Path(user_file)

if file_path.exists() and file_path.is_file():
    print("File found")
else:
    print("File not found")
