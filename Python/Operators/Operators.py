# Arithmetic Operators
print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)

# Relational Operators
print(4 > 5)
print(4 < 5)
print(4 >= 4)
print(4 <= 4)
print(4 == 4)
print(4 != 4)

# Logical Operators
print(1 and 0)
print(1 or 0)
print(not 1)

# Bitwise Operators
print(2 & 3)  # bitwise and
print(2 | 3)  # bitwise or
print(2 ^ 3)  # bitwise xor
print(~3)     # bitwise not
print(4 >> 2) # bitwise right-shift The newly introduced bits are chosen by interpreter
print(5 << 2) # bitwise left-shift The newly introduced bits are 0

# Assignment Operators
a = 2
a %= 2  # a = a % 2
print(a)

# Membership Operators
print('D' not in 'Delhi')
print(1 in [2, 3, 4, 5, 6])

# Identity Operator
f, g = 12, 13
print(f is g)
print(3 is 4)
print("f is not g:", f is not g)  # False

# Immutability of Integers: In Python, integers are immutable. This means that once an integer object is created, its value cannot be changed. When you perform an operation that seems to modify an integer (like assigning a new value), Python actually creates a new integer object instead of modifying the existing one
# This is only possible with integers and booleans

a = True
b = True
print(a is b)

h = [1, 2, 3]
i = [1, 2, 3]

print("h is i:", h is i)           # False, because 'h' and 'i' are different instances even if they have the same content
print("h is not i:", h is not i)   # True

dict1 = {1:'hi'}
dict2 = {1:'hi'}
print(dict1 is dict2)              # False
print(dict1 == dict2)              # True

# Exceptional Cases
# Arithmetic Operator Division by Zero
try:
    print("\nExceptional Case (Arithmetic Division by Zero):")
    print("Division (a / 0):", a / 0)  # Raises ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)

# Logical Operator with Non-Boolean Types
print("\nExceptional Case (Logical Operator with Non-Boolean Types):")
print("'Hello' and 5:", 'Hello' and 5)  # 'Hello' (truthy) and 5 (truthy), so result is 5

print('aaaaaa' and 5 and 'true') # 'True'

# Membership Operator with Different Data Types
print("\nExceptional Case (Membership Operator with Different Data Types):")
print("'a' in [1, 2, 3]:", 'a' in [1, 2, 3])  # False, 'a' is not in the list of integers

# Identity Operator with Different Data Types
print("\nExceptional Case (Identity Operator with Different Data Types):")
print("[] is []:", [] is [])  # False, because they are different instances

# Difference between == and is
'''
== operator compares just the values
is operator compares the identity of variables -> True if both the variables are pointing to same memory location

Immutable Types: For some immutable types like small integers and strings, Python may reuse objects for efficiency. For example:
a = 1000
b = 1000
print(a == b)  # True
print(a is b)  # True (due to internal optimization in CPython for small integers)
'''

# Program - Find the sum of a 3 digit number entered by the user
number = int(input('Enter a 3 digit number: '))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
print(a + b + c)