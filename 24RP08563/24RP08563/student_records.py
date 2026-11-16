# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Consolidated Python File Handling Practical Exercise (Tasks 1 to 8)

import os
from pathlib import Path

print("================ TASK 1: Create a new file ================")
if os.path.exists("students.txt"):
    os.remove("students.txt")

with open("students.txt", "x") as file:
    file.write("101, Alice, IT\n")
    file.write("102, Eric, Electronics\n")
    file.write("103, Diane, IT\n")
print("students.txt created with 3 records.")

try:
    with open("students.txt", "x") as file:
        file.write("Test\n")
except FileExistsError as e:
    print("Running mode 'x' again raises:", type(e).__name__, "-", e)

print("\n================ TASK 2: Open and read a file ================")
print("1. Entire contents:")
with open("students.txt", "r") as file:
    print(file.read(), end="")

print("\n2. First line only:")
with open("students.txt", "r") as file:
    print(file.readline(), end="")

print("\n3. Loop through each record:")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n================ TASK 3: Investigate read access ================")
with open("students.txt", "r") as file:
    print("readable():", file.readable())
    print("writable():", file.writable())
    # file.write("104, Claude, IT\n")  # Commented out: raises io.UnsupportedOperation: not writable

print("\n================ TASK 4: Add information to an existing file ================")
with open("students.txt", "a") as file:
    file.write("104, Claude, IT\n")
    file.write("105, Aline, Electronics\n")

with open("students.txt", "r") as file:
    student_lines = [line.strip() for line in file if line.strip()]

for record in student_lines:
    print(record)
print("Total number of students:", len(student_lines))

print("\n================ TASK 5: Replace existing contents ================")
with open("announcement.txt", "w") as file:
    file.write("Python practical starts at 09:00.\n")

with open("announcement.txt", "w") as file:
    file.write("Python practical starts at 10:00.\n")

with open("announcement.txt", "r") as file:
    print("announcement.txt content:", file.read().strip())

print("\n================ TASK 6: Check whether a file exists ================")
# Demonstrating with user input (and fallback if run non-interactively)
try:
    filename = input("Enter filename (e.g., students.txt or missing.txt): ")
except EOFError:
    filename = "students.txt"

path = Path(filename)
if path.exists() and path.is_file():
    print("File found")
else:
    print("File not found")

print("\n================ TASK 7: Delete a practice file ================")
with open("temporary.txt", "w") as file:
    file.write("Temporary practice content.\n")

if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
    print("temporary.txt deleted.")

if not os.path.isfile("temporary.txt"):
    print("Confirmed: temporary.txt no longer exists.")

if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
else:
    print("Second check: temporary.txt is missing (handled safely without crashing).")

print("\n================ TASK 8: Delete an empty folder ================")
os.makedirs("practice_backup", exist_ok=True)
note_file = os.path.join("practice_backup", "note.txt")
with open(note_file, "w") as file:
    file.write("Temporary backup note.\n")

try:
    os.rmdir("practice_backup")
except OSError as e:
    print("Error removing non-empty folder:", type(e).__name__, "-", e)

if os.path.isfile(note_file):
    os.remove(note_file)
os.rmdir("practice_backup")

if not os.path.exists("practice_backup"):
    print("Confirmed: practice_backup folder deleted after removing note.txt.")
