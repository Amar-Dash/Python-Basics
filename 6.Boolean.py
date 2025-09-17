#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool('HELLO')) #Any string is True, except empty strings.
print(bool(15)) #Any number is True, except 0.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Any list, tuple, set, and dictionary are True, except empty ones.
#False values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0

myop = myclass()
print(bool(myop)) 