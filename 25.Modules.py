import mymodule as my
print(my.welcome('Amar'))

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Example
# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)