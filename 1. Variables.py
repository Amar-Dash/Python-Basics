#Variables in python

x=223
name='Amar'
print(x,"and", name)

#Casting - changes the the type of variable, here a interger is converted into string
x=str(2)
y=str(3)
print(x+y)

#Getting the Type - by using type() you can get the type of the var. printed
x='Pragyan'
print(type(x))

#A var. can't start with a number, only with underscore
#It can't be a python keyword nad should be alpha-numeric and underscores

#Case of writing big varibables

myVaribaleName = 'Amar' #This is known as 'Camel Case' - all the words are capital except first
MyVaribaleName = 'Amar' #This is known as 'Pascal Case' - all the words are capital
my_varibale_name = 'Amar' #This is known as 'Snake Case' - all the words are separated by underscore

#Multiple var. in one line with multiple value

x, y, z = 1, 2, 3
print(x,",",y, 'and', z)

#Unpacking a collection

fruits = ['apple', 'banana', "orange"]
x, y, z = fruits
print(x,y,z)

#Global Var.
#It is created outside the fn.
def myfunc():
  x = "fantastic"

myfunc()

print("Python is " + x) #Here it prints Pyrhon is apple - because x is local var. and the global x is apple
#But, if I do this then,
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)#Now it prints Python is fantastic  