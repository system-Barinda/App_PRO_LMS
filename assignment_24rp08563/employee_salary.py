# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 5: Employee Salary Management

def calculate_salary() -> None:
    name: str = "System Sylvere Barinda"
    basic: float = 250000.0
    transport: float = 30000.0
    housing: float = 50000.0
    
    gross_salary = basic + transport + housing
    print(f"Employee: {name}")
    print(f"Basic: {basic} | Transport: {transport} | Housing: {housing}")
    print(f"Gross Salary: {gross_salary:,.2f} RWF")

if __name__ == "__main__":
    calculate_salary()
