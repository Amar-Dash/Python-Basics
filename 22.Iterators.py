# # An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# # Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# The for loop actually creates an iterator object and executes the next() method for each loop.


# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class Mynum:
    def __iter__(self): 
        self.a=1
        return self

    def __next__(self):
        x=self.a
        x =+ 1
        return x
    
myclass = Mynum()
myiter = iter(myclass)

print(next(myiter))

#Stopping
    #  def __next__(self):
    # if self.a <=20:
    #     x=self.a
    #     x =+ 1
    #     return x
    # else:
    #     raise StopIteration
