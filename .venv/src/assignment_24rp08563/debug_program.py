# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 3: Debugging a Python Program

def display_results() -> None:
    student_name: str = "FNAME"
    marks: int = 85
    
    print("Student:", student_name)
    if marks >= 50:
        print("Passed")
    else:
        print("Failed")


if __name__ == "__main__":
    display_results()
