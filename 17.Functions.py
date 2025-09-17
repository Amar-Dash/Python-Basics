def myfn():
    print("Amar")

myfn()

def myfn2(fname):
    print(fname + 'op')

myfn2("Email")

# Arbitary Args

def opfn(*argsi):
    print("Amar is op" + argsi[1])

opfn("for he is op", "shopi")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0): 
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# / -- for positional args
# * -- for kwargs, also can combine both