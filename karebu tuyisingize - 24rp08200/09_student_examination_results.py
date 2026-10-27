# Student Name: Tuyisingize Karebu 
# Registration Number: 24RP08200
# Python and Fundamentals of AI - Learning Unit 2

# Question 9: Student Examination Results

python_marks = 85
database_marks = 78
networking_marks = 92


total_marks = python_marks + database_marks + networking_marks
average_marks = total_marks / 3
average_text = str(average_marks)

print("===== STUDENT EXAMINATION RESULTS =====")
print("Student:", "Tuyisingize Karebu ")
print("Python Programming:", python_marks)
print("Database Management:", database_marks)
print("Computer Networking:", networking_marks)
print("Total marks:", total_marks)
print("Average marks: " + average_text)

print("\n===== DATA TYPES =====")
print("Total marks:", type(total_marks))
print("Average marks:", type(average_marks))
print("Converted average:", type(average_text))
