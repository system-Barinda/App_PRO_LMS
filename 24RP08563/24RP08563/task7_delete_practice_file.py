# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 7: Delete a practice file
# 1. Create temporary.txt, write a short message in it, and close it.
# 2. Check whether it exists and delete it using os.remove().
# 3. Check again and display a message confirming deletion.
# 4. Run the deletion code again. Report that the file is missing without crashing.

import os

# 1. Create temporary.txt, write message, and close it
with open("temporary.txt", "w") as file:
    file.write("This is a temporary practice file.\n")
print("Created temporary.txt")

# 2. Check whether it exists and delete it
if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
    print("temporary.txt found and deleted.")

# 3. Check again and confirm deletion
if not os.path.isfile("temporary.txt"):
    print("Confirmation: temporary.txt no longer exists.")

# 4. Run deletion code again safely without crashing
if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
else:
    print("Safe check: Cannot delete temporary.txt because the file is missing.")
