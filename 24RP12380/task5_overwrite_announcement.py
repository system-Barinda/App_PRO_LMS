# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 5: Replace existing contents using mode "w"
# Question: How does "w" differ from "a"?
# Answer: Mode "w" erases old text and replaces it, while mode "a" keeps old text and adds new text at the end.

# First write
with open("announcement.txt", "w") as ann_file:
    ann_file.write("Python practical starts at 09:00.\n")

# Second write (replaces first)
with open("announcement.txt", "w") as ann_file:
    ann_file.write("Python practical starts at 10:00.\n")

# Read and display result
with open("announcement.txt", "r") as ann_file:
    message = ann_file.read()
    print("Current announcement:", message.strip())
