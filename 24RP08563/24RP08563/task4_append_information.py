# Student Name: BARINDA System Sylvere
# Registration Number: 24RP08563
# Department: ICT - Class: Year 3 - IT
# Module: Python and Fundamentals of AI

# Task 4: Add information to an existing file
# 1. Open students.txt using mode "a".
# 2. Add two new records (104, Claude, IT and 105, Aline, Electronics).
# 3. Read the file and display all records.
# 4. Count and display the number of students.
# Question: What happens if you run the append statements twice?
# Answer: The two new records will be added to the end of the file a second time, resulting in duplicate entries (7 records total instead of 5).

with open("students.txt", "a") as file:
    file.write("104, Claude, IT\n")
    file.write("105, Aline, Electronics\n")

with open("students.txt", "r") as file:
    records = [line.strip() for line in file if line.strip()]

print("All student records after appending:")
for record in records:
    print(record)

print(f"Total number of students: {len(records)}")
