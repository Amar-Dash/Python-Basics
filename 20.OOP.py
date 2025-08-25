class My:
    x=5
p1 = My()
print(p1.x)

# #All classes have a method called __init__(), which is always executed when the class is being initiated.
# Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class

class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

P = Person('Amar', 15, 'Male')
print(P.name)

#  The __init__() method is called automatically every time the class is being used to create a new object.

# The __str__() method controls what should be returned when the class object is represented as a string.
# If the __str__() method is not set, the string representation of the object is returned:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}, {self.age}"
P = Person('Amar', 15,)
print(P)

# modify
P.name = 'John'
# delete obj and properties
del P.age
del P

