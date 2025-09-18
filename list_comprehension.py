"""List comprehensions = a concise way to create lists
in python.  Compact and easier to read than traditional loops
[expression for singularvalue in iterable if condition]"""


#traditional loop

doubles = [] #empty list or array

for x in range(1, 11):  #second argument is exclusive
    doubles.append(x * 2)
    
print(doubles)   


#loop rewritten as list comprehension
dubles = [x * 2 for x in range(1, 11)]

print(dubles)
    
    