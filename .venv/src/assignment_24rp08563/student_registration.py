# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 1: Student Registration System

def register_student() -> None:
    print("--- STUDENT REGISTRATION ---")
    name = input("Full Name: ")
    reg_no = input("Registration Number: ")
    dept = input("Department: ")
    year = input("Academic Year: ")
    phone = input("Telephone: ")
    
    report = f"""
STUDENT REGISTRATION
Full Name: {name}
Registration Number: {reg_no}
Department: {dept}
Academic Year: {year}
Telephone: {phone}
Registration completed successfully!
"""
    print(report)

if __name__ == "__main__":
    register_student()
