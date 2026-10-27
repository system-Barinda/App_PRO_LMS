# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 2: Electricity Billing System

def calculate_bill() -> None:
    RATE_PER_UNIT: float = 250.0  # RWF per unit
    units = float(input("Enter electricity units consumed: "))
    total_cost = units * RATE_PER_UNIT
    
    print(f"Units Consumed: {units}")
    print(f"Rate per Unit: {RATE_PER_UNIT} RWF")
    print(f"Estimated Total Bill: {total_cost:,.2f} RWF")
    # Example: 35 units cost an estimated 8,750 RWF.

if __name__ == "__main__":
    calculate_bill()


24rp08200;
