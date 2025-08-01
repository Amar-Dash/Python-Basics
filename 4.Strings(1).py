#In python the strings are array 
for x in 'apple':
    print(x)

#Check the presence of word
op = 'i am Amar'
print('Amar' in op)

if 'Amar' in op:
    print('Yes')
else:
    print('No')

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
name="Amar"
print(name[2:3])
#By leaving out the start index, the range will start at the first character:
print(name[:4])
#By leaving out the end index, the range will go to the end:
print(name[0:])
#Negative Indexing
op = " Amar is OP "
print(len(op))
x =op[1:-5]
print(x, len(x))
#How it works
#print(op[1:len(op)-5])

#String Meathods

#Upper Case
print(op.upper())
#Lower Case
print(op.lower())
#Remove Whitespaces
print(op.strip())
#Replace
print(op.replace('A', 'S'))
#Split
print(op.split( ))

#String Concatination :- Very Easy bro