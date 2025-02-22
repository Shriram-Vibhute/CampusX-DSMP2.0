# Required arg and default arg
def average(a, b = 0):
    return ((a + b)/2)
a = int(input("Enter the first value : "))
b = int(input("Enter the first value : "))
avg = average(a, b) # b will get overrided in function
print(avg)
average(a)
print(avg)
# average() -> Gives an error - a is required arg

# Keyword arbitrary arguments
def sequence(a, b):
    print(a + b)
sequence(b = 45, a = 87)

# Passing arg as a tuple
def mean(*array):
    print(type(array))
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
    meanVal = (sum/len(array))
    return meanVal

print(mean(1,2,3,4,5,6,7)) 
# print(mean([1,2,3])) - *arr treat all the arguments as list not like original list we are passing

# Passing arg as Dictonary
def printVal(**dict):
    print(dict["name"], dict["country"]) # Make sure the keys are in double quotes
printVal(name = "Dexter", country= "USA", gangstar_id= 69,)# Make sure the keys are not in double quotes
# You cannot do like this
"""
dummyDict = {
    "name": "a",
    "surname": "b",
}
printVal(dummyDict)
"""

# pass keyword - for declaring functions
def passFunction():
    pass

# You can use pass statement in loops, if else, functions, match-case etc -> for passing that perticular intance of execution

def dict_func(*args, **kwargs):
    print(args)
    print(kwargs)
dict_func(1,2,3,4, a = 1,b = 2)
# Normal parameters you provide are called positional arguments