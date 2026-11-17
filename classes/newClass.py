# class Barinda:
#      x = 100
     
# system = Barinda()
# print( 5 * system.x);     


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
# newPerson = Person("Barinda",23)
# print(newPerson.name);        
# print(newPerson.age);        

# class Person:
#     def __init__(self, name= 'barinda system sylvere',age= 23):
#         self.name = name
#         self.age = age

# person1 = Person("My mon I love her more");

# print(person1.name)       

# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Barinda :
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def desplay(self):
#         print("Name : ", self.name)
#         print("Age : ", self.age)
# newPerson = Person("barinda",21)
# newPerson.desplay()            

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def printname(self):
#     print(self.name)

# p1 = Person("Tobias")
# p2 = Person("Linus")

# p1.printname()
# p2.printname()


# class Person:
#     def __init__(barinda,name,age):
#           barinda.name = name
#           barinda.age = age
          
#     def display(t):
#         print("name is :", t.name)
#         print("age is :", t.age)
        

# newPerson = Person("iradukunda sandrine", 25);

# newPerson.display()              

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()