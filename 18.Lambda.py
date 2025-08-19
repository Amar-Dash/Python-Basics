x = lambda a: a+10
print(x(5))

def myfn(a,n):
    return lambda a: a*n
mydoubler = myfn(2)
print(mydoubler(3))

