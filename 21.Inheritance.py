# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

#Parent class
class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"I am {self.name}, age is {self.age}."
    
x=Person("Amar", 15)
print(x)

#Child clas
class Student(Person):
    pass

y=Student('OP', 35)
print(y)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student1(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.graduationyear= 2019
z = Student1("Amar", 15)
print(z)
print(z.graduationyear)

class Student3(Person):
    def __init__(self,name, age, Gyear):
        self.name=name 
        self.age=age
        self.Gyear=Gyear
    
    def welcome(self):
        return f"Welcome {self.name}"
    
t=Student3('Amar', 15, 2019)
print(t.welcome())