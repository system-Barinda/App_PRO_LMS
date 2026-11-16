# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 5: Replace existing contents
# 1. Create announcement.txt using mode "w" and write the first announcement.
# 2. Open the same file again using "w" and write the second announcement.
# 3. Read the file and display its contents.
# Question: How does "w" differ from "a"?
# Answer: Mode "w" (write) truncates/erases all existing content in the file before writing new data (overwriting it), whereas mode "a" (append) preserves existing data and adds new content at the end of the file.

with open("announcement.txt", "w") as file:
    file.write("Python practical starts at 09:00.\n")

with open("announcement.txt", "w") as file:
    file.write("Python practical starts at 10:00.\n")

with open("announcement.txt", "r") as file:
    print("Contents of announcement.txt:", file.read().strip())
