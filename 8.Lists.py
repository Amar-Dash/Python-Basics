#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# #List items are ordered - it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list, changeable - The list is changeable, meaning that we can change, add, and remove items in a list after it has been created, and allow duplicate values - Since lists are indexed, lists can have items with the same value.
# # List items are indexed, the first item has index [0], the second item has index [1] etc.

# Duplicate Values
thelist=['apple','banana', 'apple', 'etc', 'banana']
print(thelist)
print(len(thelist))#This tells the no. of items in the list

# The list constructor
x = list(('apple', 'amar', 'op'))
print(x)
print(type(x))

#Acessing the list item
mylist = ['apple', 'red', 'banana']
print(mylist[1])

#Here also we can do indexing just like the strings. So no need to do it here as it will waste my time so ......

# Existance
if 'apple' in mylist: 
    print('Yes')

#Change the value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Of range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#If I insert more items than I replace, the new items will be inserted where I specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#If I insert less items than I replace, the new items will be inserted where I specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# To add items we can use .insert, .extend, .append

#Insert Items
thislist.insert(2, 'Amar')
print(thislist)

#Append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove List items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there the more than one item which has to be removed then the first occurance is removed
#To remove specific index we have (Lol I was trying this in the remove())
thislist.pop(0)
print(thislist)
#Also
del thislist[0]
print(thislist) #Lol thislist is now empty
#clear() delets all the content in the list but not itself.

#Looping through a list.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[0:2])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Without using the list comprehension this is so long to arrange a list and make an new one:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#But....
fruits = ["apple", "banana", "mango", "kiwi", "cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#if x != "apple" will return true other than apple

#Sort List
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

def myfunction(n):
  return abs(n-50)
thislist=[100, 20, 180, 51]
thislist.sort(key=myfunction)
print(thislist)

#Case Sensetive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Copy List'
mylist=thislist.copy()
print(mylist)
# Or
mylist=list(thislist)
print(mylist)

#Joining List
# By using +
thislist = ["banana", "Orange", "Kiwi", "cherry"]
fruits = ["apple", "banana", "mango", "kiwi", "cherry"]
mylist = thelist + fruits
print(mylist)

#Append
for x in fruits:
  thelist.append(x)
print(thelist)

# Using Extend
thelist.extend(fruits)
print(thelist)