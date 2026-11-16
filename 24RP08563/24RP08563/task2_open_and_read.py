# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 2: Open and read a file
# 1. Open students.txt using mode "r" and display its entire contents.
# 2. Open it again and display only the first line.
# 3. Open it again and use a loop to display each record.
# Questions:
# - What does "r" allow? Allows read-only access to the file.
# - Why use with open(...)? It acts as a context manager that automatically closes the file when the block exits, preventing resource leaks even if an error occurs.
# - What happens if the file does not exist? Python raises a FileNotFoundError.

print("--- 1. Entire contents using read() ---")
with open("students.txt", "r") as file:
    print(file.read(), end="")

print("\n--- 2. First line only using readline() ---")
with open("students.txt", "r") as file:
    print(file.readline(), end="")

print("\n--- 3. Each record using a loop ---")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
