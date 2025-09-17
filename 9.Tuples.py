#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Making it through constructor
x = tuple('apple')
print(type(x))

#We can access tuple items and can check any items avail. just like list
if 'apple' in thistuple:
    print("YES")

#Since tuples are immutable there is no append function.
#But we can change values of tuple in couple of different ways

#Making the tuple a list
x = list(thistuple)
x[1] = 'etc'
x.append("Amar")
thistuple = tuple(x)
print(type(thistuple))
print(thistuple)

#Concatinating two tuples
y = ("orange",)
thistuple += y
print(thistuple) 

#Same for removing also
#Unpacking tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop tupels
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i = i+1

#Multiply tuples
thistuple = ("apple", "banana", "cherry")
op = thistuple *2
print(op)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

