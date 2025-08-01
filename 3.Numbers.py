#There are total 3 types of numbers in python
'''
1.int
2.float
3.complex
'''

x=1
y=18.0
z=18j

print(type(x), type(y), type(z))

#Int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

#Float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.Float can also be scientific numbers with an "e" to indicate the power of 10.

#Complex - Complex numbers are written with a "j" as the imaginary part

#Conversion
a = complex(x)
b = float(x)
c = int(y)
#You can't change complex no. to any other
print(a,b,c)

#Random number
import random
print(random.randrange(10)) #Print any random no. for 0-9