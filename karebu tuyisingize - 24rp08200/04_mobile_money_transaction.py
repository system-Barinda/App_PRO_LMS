# Student Name: Tuyisingize Karebu 
# Registration Number: 24RP08200
# Python and Fundamentals of AI - Learning Unit 2

# Question 4: Mobile Money Transaction Record

customer_name = "Tuyisingize Karebu "
initial_balance = float(input("Enter initial balance (RWF), e.g. 150000: "))
withdrawal_amount = float(input("Enter withdrawal amount (RWF), e.g. 45000: "))
transaction_fee = 500

remaining_balance = initial_balance - withdrawal_amount - transaction_fee

print("\n===== MOBILE MONEY TRANSACTION =====")
print("Customer:", customer_name)
print("Initial balance:", initial_balance, "RWF")
print("Withdrawal:", withdrawal_amount, "RWF")
print("Transaction fee:", transaction_fee, "RWF")
print("Remaining balance:", remaining_balance, "RWF")
