# Arithmetic Operators
a = 10
b = 5
        
print("Arithmetic Operators:")
print("Addition (a + b):", a + b)           # 15
print("Subtraction (a - b):", a - b)        # 5
print("Multiplication (a * b):", a * b)     # 50
print("Division (a / b):", a / b)           # 2.0
print("Floor Division (a // b):", a // b)   # 2
print("Modulus (a % b):", a % b)            # 0
print("Exponentiation (a ** b):", a ** b)   # 100000

# Logical Operators
x = True
y = False

print("\nLogical Operators:")
print("Logical AND (x and y):", x and y)    # False
print("Logical OR (x or y):", x or y)      # True
print("Logical NOT (not x):", not x)       # False

# Assignment Operators
c = 10

print("\nAssignment Operators:")
c += 5   # c = c + 5
print("Addition Assignment (c += 5):", c)  # 15
c -= 3   # c = c - 3
print("Subtraction Assignment (c -= 3):", c)  # 12
c *= 2   # c = c * 2
print("Multiplication Assignment (c *= 2):", c)  # 24
c /= 6   # c = c / 6
print("Division Assignment (c /= 6):", c)  # 4.0
c **= 2  # c = c ** 2
print("Exponentiation Assignment (c **= 2):", c)  # 16.0

# Comparison Operators
d = 10
e = 20

print("\nComparison Operators:")
print("Equal to (d == e):", d == e)          # False
print("Not equal to (d != e):", d != e)     # True
print("Greater than (d > e):", d > e)       # False
print("Less than (d < e):", d < e)          # True
print("Greater than or equal to (d >= e):", d >= e)  # False
print("Less than or equal to (d <= e):", d <= e)    # True

# Membership Operators
lst = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("1 in lst:", 1 in lst)       # True
print("6 not in lst:", 6 not in lst)  # True

# Identity Operators
f = 10
g = 10

print("\nIdentity Operators:")
print("f is g:", f is g)          # True, because integers are immutable and 'f' and 'g' point to the same object
print("f is not g:", f is not g)  # False

h = [1, 2, 3]
i = [1, 2, 3]

print("h is i:", h is i)           # False, because 'h' and 'i' are different objects even if they have the same content
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