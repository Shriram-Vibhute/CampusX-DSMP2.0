# Let's create a function (with docstring)

def is_even(num):
  """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 16th Nov 2022
  """
  if type(num) == int:
    if num % 2 == 0:
      return 'even'
    else:
      return 'odd'
  else:
    return 'pagal hai kya?'

for i in range(1,11):
  x = is_even(i)
  print(x)

print(type.__doc__)

# 2 Point of views
is_even('hello') # Those who are creating a functions must handle all the possible edge cases and does not stop the execution because of some error

# Parameters Vs Arguments
'''
parameters - Those which are given when the function was creating
arguments - Those which are passed during calling
'''

### Types of Arguments
'''
- Default Argument
- Positional Argument
- Keyword Argument
'''

def power(a=1,b=1):
  return a**b

power()

# positional argument
power(2,3)

# keyword argument
power(b=3,a=2)

# `*args and **kwargs`
'''
`*args and **kwargs` are special Python keywords that are used to pass the variable length of arguments to a function
'''

# *args - allows us to pass a variable number of non-keyword arguments to a function.

def multiply(*args): # Accept all the arguments as tuple
  product = 1

  for i in args:
    product = product * i

  print(args)
  return product

multiply(1,2,3,4,5,6,7,8,9,10,12)

# **kwargs - kw -> keyword
'''
**kwargs allows us to pass any number of keyword arguments.
Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
'''

def display(**kwargs): # Accept all the arguments as dictonary
  for (key,value) in kwargs.items():
    print(key,'->',value)

display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad') # Everything must be keyword args

# Points to remember while using `*args and **kwargs
'''
- order of the arguments matter(normal -> `*args` -> `**kwargs`)
- The words “args” and “kwargs” are only a convention, you can use any name of your choice
'''

def dummy(a, b, *args, **kwargs): # The order of initilizing this parameters also should me maintained - positional -> Keyword -> Default
  print(a, b)
  print(args)
  print(kwargs)

dummy(4, 5, 6, f = 10, g = 11, a = 5, b = 50) # We cannot pass args like this - The order should be maintained

# How Functions are executed in memory?
'''
When the function is called, a seperate a block of memory will be created inside your RAM and this block will be destroyed after function return something

If function does not have return statment then by default function returns None
'''

# Without return statement

L = [1,2,3]
print(L.append(4)) # append function is inplace operation - Thats why returns NONE
print(L)

# Variable Scope

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def f(y):
    x = 1 # This is local
    x += 1
    print(x)
x = 5
f(x)
print(x)

x = 5
def h(y):
    x += 1 # Error - You cannot do something like these inside a function without creating a local variable
h(x)
print(x)

def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

# Using global variables inside the functions
a = 10
def dummy(var):
  # a = 34 - you cannot initilize global var before golbal indication in funtion
  global a
  # a = 20 - you are updating the global value of a
  print(a)
dummy(10)

# You can access global variables into loval score but you cannot modify them until and unless you mention global keyword - But this is not a good practice because is could be possible that others functions also using those value

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

type(square)
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

# Benefits of using a Function
'''
- Code Modularity
- Code Readibility
- Code Reusability
'''

# Lambda Function
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression. 
'''

# x -> x^2
lambda x:x**2

# x,y -> x+y
a = lambda x,y:x+y
a(5,2)

# Diff between lambda vs Normal Function
'''
- No name
- lambda has no return value(infact,returns a function)
- lambda is written in 1 line
- not reusable - not correct completly

Then why use lambda functions?
They are used with HOF
'''

# check if a string has 'a'
a = lambda s:'a' in s
a('hello') # We can reuse lambda function like this throught the code.

# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
a(6)

# Higher Order Functions - A function which returns another function or a function which takes another function as argument

def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)

# Map

# square the items of a list
list(map(lambda x:x**2, [1,2,3,4,5]))

# odd/even labelling of list items
L = [1,2,3,4,5]
list(map(lambda x:'even' if x%2 == 0 else 'odd',L))

# fetch names from a list of dict

users = [
  {
    'name':'Rahul',
    'age':45,
    'gender':'male'
  },
  {
    'name':'Nitish',
    'age':33,
    'gender':'male'
  },
  {
    'name':'Ankita',
    'age':50,
    'gender':'female'
  }
]

print(list(map(lambda users:users['gender'],users)))

# Filter

# numbers greater than 5
L = [3,4,5,6,7]

list(filter(lambda x:x>5,L))

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

list(filter(lambda x:x.startswith('a'),fruits))

"""### Reduce"""

# sum of all item
import functools

functools.reduce(lambda x,y:x+y,[1,2,3,4,5])

# find min
functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1])

print(functools.reduce(lambda a, b, c: a + b + c, [1,2,3,4,5])) # Cannot work with more than 2 parameters