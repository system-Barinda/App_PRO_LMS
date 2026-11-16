# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 8: Delete an empty folder
# Question: Why does os.rmdir() fail when the folder contains a file?
# Answer: os.rmdir() only deletes empty folders to protect files inside from being lost accidentally.

import os

# 1. Create practice_backup folder
os.makedirs("practice_backup", exist_ok=True)

# 2. Create note.txt inside practice_backup
note_file = os.path.join("practice_backup", "note.txt")
with open(note_file, "w") as f:
    f.write("Hello backup folder.\n")

# 3. Try deleting non-empty folder and observe error
try:
    os.rmdir("practice_backup")
except OSError as error:
    print("Could not delete non-empty folder:", error)

# 4. Delete note.txt first, then remove the empty folder
if os.path.isfile(note_file):
    os.remove(note_file)

os.rmdir("practice_backup")

# 5. Confirm folder no longer exists
if not os.path.exists("practice_backup"):
    print("Verified: practice_backup folder has been removed.")
