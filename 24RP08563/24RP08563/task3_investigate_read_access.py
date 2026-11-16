# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 3: Investigate read access
# 1. Open students.txt using mode "r".
# 2. Display file.readable() and file.writable().
# 3. Try writing "104, Claude, IT\n" while the file is open in "r" mode.
# 4. Record the error, then remove or comment out the failing statement.
# Recorded Error: io.UnsupportedOperation: not writable

with open("students.txt", "r") as file:
    print("readable():", file.readable())
    print("writable():", file.writable())
    
    # Failing statement commented out after observing the error:
    # file.write("104, Claude, IT\n")  # Raises io.UnsupportedOperation: not writable
