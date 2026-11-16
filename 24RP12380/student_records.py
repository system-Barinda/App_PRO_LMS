# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Main Submission Program: student_records.py (Tasks 1 to 8)

import os
from pathlib import Path

# --- TASK 1: Create students.txt ---
print("--- Task 1 ---")
if os.path.exists("students.txt"):
    os.remove("students.txt")

initial_students = [
    "101, Alice, IT\n",
    "102, Eric, Electronics\n",
    "103, Diane, IT\n"
]
with open("students.txt", "x") as f:
    f.writelines(initial_students)
print("Created students.txt with 3 students.")

# --- TASK 2: Open and read students.txt ---
print("\n--- Task 2 ---")
with open("students.txt", "r") as f:
    print("All records:\n" + f.read().strip())

with open("students.txt", "r") as f:
    print("First line:", f.readline().strip())

print("Looping lines:")
with open("students.txt", "r") as f:
    for line in f:
        print(" *", line.strip())

# --- TASK 3: Investigate read access ---
print("\n--- Task 3 ---")
with open("students.txt", "r") as f:
    print("readable():", f.readable())
    print("writable():", f.writable())
    # f.write("104, Claude, IT\n")  # Fails with io.UnsupportedOperation: not writable

# --- TASK 4: Append new students ---
print("\n--- Task 4 ---")
with open("students.txt", "a") as f:
    f.write("104, Claude, IT\n")
    f.write("105, Aline, Electronics\n")

total = 0
with open("students.txt", "r") as f:
    for line in f:
        if line.strip():
            print(line.strip())
            total += 1
print("Total students:", total)

# --- TASK 5: Replace announcement.txt ---
print("\n--- Task 5 ---")
with open("announcement.txt", "w") as f:
    f.write("Python practical starts at 09:00.\n")

with open("announcement.txt", "w") as f:
    f.write("Python practical starts at 10:00.\n")

with open("announcement.txt", "r") as f:
    print("Announcement:", f.read().strip())

# --- TASK 6: Check file existence ---
print("\n--- Task 6 ---")
for test_name in ["students.txt", "missing.txt"]:
    p = Path(test_name)
    status = "File found" if (p.exists() and p.is_file()) else "File not found"
    print(f"Checking {test_name}: {status}")

# --- TASK 7: Delete practice file ---
print("\n--- Task 7 ---")
with open("temporary.txt", "w") as f:
    f.write("Temporary practice text.\n")

if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
    print("temporary.txt deleted.")

if not os.path.isfile("temporary.txt"):
    print("Confirmed: temporary.txt no longer exists.")

if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
else:
    print("Second check: temporary.txt is missing (no crash).")

# --- TASK 8: Delete empty folder ---
print("\n--- Task 8 ---")
os.makedirs("practice_backup", exist_ok=True)
note_path = os.path.join("practice_backup", "note.txt")
with open(note_path, "w") as f:
    f.write("Note inside folder.\n")

try:
    os.rmdir("practice_backup")
except OSError as err:
    print("Expected error on non-empty folder:", err)

os.remove(note_path)
os.rmdir("practice_backup")
if not os.path.exists("practice_backup"):
    print("Confirmed: practice_backup folder deleted.")
