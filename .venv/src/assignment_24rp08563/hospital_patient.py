# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 7: Hospital Patient Registration

def register_patient() -> None:
    name: str = "System Sylvere Barinda"
    age: int = 32
    temp: float = 37.2
    admitted: bool = True
    phone: str = "0780000000"
    
    for var in [name, age, temp, admitted, phone]:
        print(f"Value: {var} | Type: {type(var)}")

if __name__ == "__main__":
    register_patient()
