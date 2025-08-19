amar = ['ban', 'puid', 'gokha']
for i in amar:
    print(i)
    for x in i:
        print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in fruits:
  if x == "banana":
    break
  print(x)

# for x in range(10001):
#    print(x)

for x in range(1, 6, 2):
   print(x)

for x in range(6):
  print(x)
  if x == 3: 
    break  
else:
  print("Finally finished!")