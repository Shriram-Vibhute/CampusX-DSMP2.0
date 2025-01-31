# 1. Lists
'''
- What are Lists?
- Lists Vs Arrays
- Characterstics of a List
- How to create a list
- Access items from a List
- Editing items in a List
- Deleting items from a List
- Operations on Lists
- Functions on Lists
'''

# What are Lists
'''
List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.
'''

# Why Lists are required in programming?
'''
Lists are required in programming because they provide a way to store multiple items in a single variable. This is useful for:
- Organizing data: Lists allow you to group related data together.
- Dynamic sizing: Lists can grow and shrink as needed, making them flexible.
- Easy access and modification: Items in a list can be accessed and modified using indexing and slicing.
- Versatility: Lists can store heterogeneous data types, including other lists.
- Built-in functions: Python provides many built-in functions and methods to manipulate lists efficiently.
'''

# Array Vs Lists
'''
- Fixed Vs Dynamic Size
- Convenience -> Hetrogeneous
- Speed of Execution
- Memory
'''

# How lists are stored in memory location
L = [1,2,3,'dexter',256]
d = 256

print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(L[3]))
print(id(1))
print(id(2))
print(id(3))
print(id('dexter'))
print(id(d))
print(id(L[4]))

d = 257
print(id(d))

M = L # The address of L is initialized to M
print(M is L)

a, b, *c = L # List unpacking concept
print(c[1] is L[len(L) - 2])

# Python does not create multiple instances of a single value. Instead, it creates one instance of a value at the start of initialization and reuses the same instance, changing the address locations of variables as needed.

# Characterstics of a List
'''
- Ordered
- Changeble/Mutable
- Hetrogeneous
- Can have duplicates
- are dynamic
- can be nested
- items can be accessed
- can contain any kind of objects in python - even the predefined functions as well.
'''

# Creating a List  

# Empty
print([])
# 1D -> Homo
print([1,2,3,4,5])
# 2D
print([1,2,3,[4,5]])
# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])
# Hetrogenous
print([1,True,5.6,5+6j,'Hello'])
# Using Type conversion
print(list('hello'))

# Accessing Items from a List

# Indexing
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
# positive
print(L[0][0][1])
# negative
print(L[-1])

# Slicing
L = [1,2,3,4,5,6]

print(L[::-1])

# Adding Items to a List

# append
L = [1,2,3,4,5]
L.append(True)
print(L)

# extend
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)

l = [1,2,3]
l.extend((4,5,6)) # Extending tuple to a list
print(l)

L = [1,2,3,4,5]
L.extend('delhi')
print(L)

L = [1,2,3,4,5]
L.append([6,7,8]) 
print(L)

# insert
L = [1,2,3,4,5]

L.insert(1,100)
print(L)

# Editing items in a List

L = [1,2,3,4,5]

# editing with indexing
L[-1] = 500

# editing with slicing
L[1:4] = [200,300,400]

print(L)

# Deleting items from a List

# del
L = [1,2,3,4,5]
# indexing
del L[-1]
# slicing
del L[1:3]
print(L)

# remove
L = [1,2,3,4,5]
L.remove(5) # Remove first occurrence of value.
print(L)

# pop
L = [1,2,3,4,5]
L.pop() # You can also provide the index
print(L)

# clear
L = [1,2,3,4,5]
L.clear()
print(L)

# Operations on Lists
'''
- Arithmetic
- Membership
- Loop
'''

# Arithmetic (+ ,*)
L1 = [1,2,3,4]
L2 = [5,6,7,8]

# Concatenation/Merge
print(L1 + L2)

print(L1*3)

L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 not in L1)
print([5,6] in L2)

# Loops
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in L3:
  print(i)

# List Functions

# len/min/max/sorted - universal func
L = [2,1,5,7,0]

print(len(L))
print(min(L)) # If your list only contains homogenous type data
print(max(L)) # If your list only contains homogenous type data
print(sorted(L,reverse=True)) # Returns any datatype into list

# count
L = [1,2,1,3,4,1,5]
L.count(5)

# index
L = [1,2,1,3,4,1,5]
L.index(1) # throws an error if element is not present 

# unlike strings there is no find method for lists

# reverse
L = [2,1,5,7,0]
# permanently reverses the list
L.reverse() # This function does not return anything
print(L)

# sort (vs sorted)
L = [2,1,5,7,0]
print(L)
print(sorted(L))
print(L)
L.sort() # Permanently sort the list
print(L)

# copy -> shallow
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))

# List Comprehension - List Comprehension provides a concise way of creating lists.
'''
Advantages of List Comprehension
- More time-efficient and space-efficient than loops.
- Require fewer lines of code.
- Transforms iterative statement into a formula.
'''

# Add 1 to 10 numbers to a list
L = []

for i in range(1,11):
  L.append(i)

print(L)

L = [i for i in range(1,11)]
print(L)

# scalar multiplication on a vector
v = [2,3,4]
s = -3
# [-6,-9,-12]

[s*i for i in v]

# Add squares
L = [1,2,3,4,5]

[i**2 for i in L]

# Print all numbers divisible by 5 in the range of 1 to 50

[i for i in range(1,51) if i%5 == 0]

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

[language for language in languages if language.startswith('p')]

# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

[fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')] # You can reframe this code using and operator

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
[[i*j for i in range(1,4)] for j in range(1,4)]

# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

[i*j for i in L1 for j in L2] # Double for loop in one comprehension

print([i * j for i in range(3) for j in range(3)]) # Nested Loop to create 1D list - runs 9 times

# 2 ways to traverse a list
'''
- itemwise
- indexwise
'''

# itemwise
L = [1,2,3,4]
for i in L:
  print(i)

# indexwise
L = [1,2,3,4]
for i in range(0,len(L)):
  print(L[i])

# Zip
'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
'''

# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

list(zip(L1,L2)) # Returns an iterator ans not directly elements

[i+j for i,j in zip(L1,L2)]


# Python can store literally any type of data even built in functions
L = [1,2,print,type,input] # can contain any kind of objects in python
print(L)

"""## Disadvantages of Python Lists

- Slow
- Risky usage
- eats up more memory
"""

a = [1,2,3]
b = a.copy()

print(a)
print(b)

a.append(4)
print(a)
print(b)
# lists are mutable