# import pandas as pd

# data = {
#     "name": ["Linus", "Amina", "Alain"],
#     "age": ["25", "30", "22"],
#     "gender": ["Male", "Female", "Male"],
#     "marks": ["85", "90", "78"],
# }

# df = pd(data)
# print(df)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()