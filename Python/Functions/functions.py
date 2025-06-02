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
printVal(name = "Dexter", country= "USA", gangstar_id= 69,) # Make sure the keys are not in double quotes
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

'''
The correct order for defining arguments in a Python function is:

Positional arguments
Default arguments
Variable length arguments (*args)
Keyword-only arguments
Variable length keyword arguments (**kwargs)
'''
def example_function(
    pos1, pos2,         # Positional arguments
    default1="value1",  # Default arguments
    *args,              # Variable length arguments
    kwonly1,            # Keyword-only arguments
    kwonly2="value2",   # Keyword-only arguments with default
    **kwargs            # Variable length keyword arguments
):
    print(pos1, pos2, default1, args, kwonly1, kwonly2, kwargs)

# Correct way to call the function:
example_function(
    1, 2,                   # pos1, pos2
    "new_default_value",    # default1
    10, 20, 30,             # *args
    kwonly1="new keyword",  # kwonly1 (must be keyword)
    kwonly2="new",          # kwonly2 (can be omitted for default)
    a1=10, a2=20, a3=30     # **kwargs
)

# Without return statement
L = [1,2,3]
print(L.append(4)) # append function is inplace operation - Thats why returns NONE
print(L)

# Nested Functions
def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')
f() # Infinite Function


def g(x):
    def h():
      x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x
x = 3
z = g(x)


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x
x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)

# Functions are 1st class citizens
'''
In general the datatypes are called as 1st class citizens but in Python the functions are also considered as 1st class citizens because functions act as a datatype in python - show below code
'''

# type and id
def square(num):
  return num**2

print(type(square)) # class function
id(square)

# reassign
x = square
id(x)
x(3)

# deleting a function
del square
square(3) # Deleted

# storing
L = [1,2,3,4,square]
L[-1](3)

# If function is datatype - is it mutable or immutable
s = {square}
s # immutable

# returning a function
def f():
    def x(a, b):
        return a+b
    return x # Here we are returning the referance of internal function

val = f()(3,4)
print(val)

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))