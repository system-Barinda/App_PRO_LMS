# marks = int(input("Enter marks: "))
# status = "adult" if marks >= 18 else "minor"
# print("Status:", status)


# def barinda():
#      print("Hello, this is a function named barinda.")
     
    
    
    
# barinda()


# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
    
# n = check_even_odd(10)

# print("The number is ", n)
    
    
# def calculate(num1,num2):
#     sum = num1 + num2
#     print("The sum is:", sum)
    
# calculate(5, 10)
    
    
    
class Student:
  
    def accept_marks(self, m1, m2, m3):
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3

    # 2. Function to calculate the sum and average
    def calculate(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        self.average = self.total / 3

    # 3. Function to display the results neatly
    def display(self):
        print("=" * 30)
        print("      STUDENT REPORT CARD     ")
        print("=" * 30)
        print(f"Subject 1 Marks : {self.mark1}")
        print(f"Subject 2 Marks : {self.mark2}")
        print(f"Subject 3 Marks : {self.mark3}")
        print("-" * 30)
        print(f"Total Marks     : {self.total}")
        print(f"Average Marks   : {self.average:.2f}")
        print("=" * 30)


# --- Running the Program ---

student1 = Student()

student1.accept_marks(85, 90, 78)
student1.calculate()
student1.display()
