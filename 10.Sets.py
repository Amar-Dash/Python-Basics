thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Don't allow duplicate valuse, unordered and unchangeable
# The values True and 1 are considered the same value in sets, and are treated as duplicates
x = set((1, 4, 10))
print(type(x), x)

#Acessing items
for x in thisset:
    print(x)
#Check presence
if "banana" in thisset:
    print(True)
print("banana" in thisset)

#You can't change items but you can add items

#By add()
thisset.add("Amar")
print(thisset)

#By update
tropical = {'op', 'shopi'}
thisset.update(tropical)
print(thisset)

#Removing

#By remove
thisset.remove('op')
print(thisset) #If item doesnot exists then it will throw an error

#By pop
thisset.pop()
print(thisset) #It will remove randomly

#By discard
thisset.discard('Amar')
print(thisset) #If item doesnot exists then also no error

#Clear empites the set
thisset.clear()
#Del deletes the set
del thisset
print(thisset)

# The union() and update() methods joins all items from both sets.

#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# The intersection() method keeps ONLY the duplicates.

#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
# You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# The difference() method keeps the items from the first set that are not in the other set(s).
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)\

#Difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# The symmetric_difference() method keeps all items EXCEPT the duplicates.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# symmetice_difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

