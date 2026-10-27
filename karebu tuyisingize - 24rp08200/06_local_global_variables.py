# Student Name: Tuyisingize Karebu 
# Registration Number: 24RP08200
# Python and Fundamentals of AI - Learning Unit 2

# Question 6: Local and Global Variables in School Management

school_name = "RP-Tumba College"  
academic_year = "Year 3"

def display_department():
    # These variables are local to this function.
    department_name = "Information Technology"
    student_population = 120
    print("School:", school_name)
    print("Department:", department_name)
    print("Student population:", student_population)

def update_academic_year():
   
    global academic_year
    academic_year = "Year 3 - Updated"

display_department()
update_academic_year()
print("Updated academic year:", academic_year)

