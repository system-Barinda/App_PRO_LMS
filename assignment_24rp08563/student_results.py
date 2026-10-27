# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 9: Student Examination Results

def calculate_results() -> None:
    python_m: float = 85.0
    db_m: float = 78.0
    net_m: float = 92.0
    
    total = python_m + db_m + net_m
    average = total / 3.0
    avg_str = str(average)
    
    print(f"Total: {total} | Average: {avg_str}")
    print(type(total), type(average), type(avg_str))

if __name__ == "__main__":
    calculate_results()
