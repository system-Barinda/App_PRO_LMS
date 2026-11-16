# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 3: Investigate read access
# Expected observations: readable() -> True, writable() -> False
# Recorded error when writing in "r" mode: io.UnsupportedOperation: not writable

with open("students.txt", "r") as student_file:
    can_read = student_file.readable()
    can_write = student_file.writable()
    print("readable():", can_read)
    print("writable():", can_write)

    # Commented out failing statement after observing error:
    # student_file.write("104, Claude, IT\n")
