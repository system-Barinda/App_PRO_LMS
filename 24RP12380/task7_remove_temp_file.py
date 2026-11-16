# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 7: Delete a practice file

import os

# 1. Create temporary.txt and write a message
with open("temporary.txt", "w") as temp_file:
    temp_file.write("Practice message inside temporary file.\n")

# 2. Check and delete using os.remove()
if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
    print("temporary.txt has been deleted.")

# 3. Confirm deletion
if not os.path.isfile("temporary.txt"):
    print("Verified: temporary.txt does not exist anymore.")

# 4. Run deletion check again safely without crashing
if os.path.isfile("temporary.txt"):
    os.remove("temporary.txt")
else:
    print("Notice: temporary.txt is already missing. No error occurred.")
