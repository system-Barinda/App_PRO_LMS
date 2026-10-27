# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 4: Mobile Money Transaction Record

def process_transaction() -> None:
    cust_name: str = "System Sylvere Barinda"
    init_bal: float = float(input("Enter initial balance: "))
    withdraw: float = float(input("Enter withdrawal amount: "))
    fee: float = 500.0
    
    rem_bal = init_bal - (withdraw + fee)
    print(f"Customer: {cust_name} | Initial: {init_bal} RWF")
    print(f"Withdrawn: {withdraw} RWF | Fee: {fee} RWF")
    print(f"Remaining Balance: {rem_bal} RWF")

if __name__ == "__main__":
    process_transaction()
