# Name: Berwa Kellia
# Registration Number: 24RP12380
# Class: Year 3 - IT | Department: ICT
# Module: Python and Fundamentals of AI

# Task 4: Add information to an existing file using mode "a"
# Question: What happens if you run the append statements twice?
# Answer: The same two students will be added again at the bottom, creating duplicate records.

with open("students.txt", "a") as student_file:
    student_file.write("104, Claude, IT\n")
    student_file.write("105, Aline, Electronics\n")

# Display all records and count them
count = 0
print("Updated student list:")
with open("students.txt", "r") as student_file:
    for row in student_file:
        clean_row = row.strip()
        if clean_row != "":
            print(clean_row)
            count = count + 1

print("Number of students:", count)
