#A var. can store diff. types of data types, with diff. purpose
x = "Hello World"		
x = 20	
x = 20.5		
x = 1j		
x = ["apple", "banana", "cherry"]		
x = ("apple", "banana", "cherry")		
x = range(6)	
x = {"name" : "John", "age" : 36}		
x = {"apple", "banana", "cherry"}	
x = frozenset({"apple", "banana", "cherry"})		
x = True		
x = b"Hello"		
x = bytearray(5)		
x = memoryview(bytes(5))	
x = None

#If I want to use specific data instead of default I have to use constructor
x = str(2)
print(type(x))