# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 6: Local and Global Variables

school_name: str = "RP-Tumba College"
academic_year: str = "Year 3"

def display_department() -> None:
    dept_name: str = "Information Technology"
    student_pop: int = 120
    print(f"School: {school_name} | Dept: {dept_name} | Students: {student_pop}")

def modify_year() -> None:
    global academic_year
    academic_year = "Year 3 Advanced"
    print(f"Updated Academic Year: {academic_year}")

if __name__ == "__main__":
    display_department()
    modify_year()
