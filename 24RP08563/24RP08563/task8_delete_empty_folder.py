# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 8: Delete an empty folder
# 1. Create practice_backup using os.makedirs("practice_backup", exist_ok=True).
# 2. Create note.txt inside that folder and close it.
# 3. Try deleting the folder using os.rmdir(). Observe the error.
# 4. Delete note.txt first, then delete the now-empty folder.
# 5. Confirm that the folder no longer exists.
# Question: Why does os.rmdir() fail when the folder contains a file?
# Answer: os.rmdir() is designed strictly to remove empty directories as a safety mechanism to prevent accidental loss of files inside a directory. It raises OSError (Directory not empty).

import os

# 1. Create practice_backup folder
os.makedirs("practice_backup", exist_ok=True)

# 2. Create note.txt inside practice_backup and close it
note_path = os.path.join("practice_backup", "note.txt")
with open(note_path, "w") as file:
    file.write("Backup note.\n")

# 3. Try deleting non-empty folder using os.rmdir()
try:
    os.rmdir("practice_backup")
except OSError as e:
    print(f"Observed error when folder is not empty: {type(e).__name__} - {e}")

# 4. Delete note.txt first, then delete the now-empty folder
if os.path.isfile(note_path):
    os.remove(note_path)
os.rmdir("practice_backup")

# 5. Confirm folder no longer exists
if not os.path.exists("practice_backup"):
    print("Confirmation: practice_backup folder has been deleted.")
