# Discrete Data Types / Data Structures
print("Int - ", 1e308)
print("Float - ", 1.46)
print("Null - ", None) # Undefined or Null

print("String - ", "Hello World")
print("Complex - ", 1+2j) 

print("Boolean - ", True)
print("BigInt - ") # In Python, there isn't actually a specific "BigInt" datatype - Python automatically handles large integers through its regular int type. This is one of Python's great features! Python's int can handle arbitrarily large numbers (limited only by your computer's memory).


# Collection Data-Types / Data-Structures
print("List - ", [1, 2, 3, 4, 5])
print("Tuple - ", (1, 2, 3, 4, 5))
print("Dictionary - ", {"Name": "John", "Age": 30})
print("Set - ", {1, 2, 3, 4, 5})


# type function
print(type(1e309))


# Dynamic Typing - Automatically detect the data type at runtime
name = 'Dexter Morgan'
age = 30 

name = "Dexter Morgan"
print(name)
name = 30
print(name)


# Compile time vs Runtime
'''
Compile Time: The phase when the code is being written
Run Time: The phase when the compiled code is executed
'''

# Multiple Assignment shorthand also called as Tuple Unpacking
a, b, c = 1, 2, 3
c = d = e = 100

# Identifiers - Naming Conventions - Basically a name given to a variable, function, class, etc.
_ = 10 # Used in Temporary or insignificant variable and Interpreter variable
# __function_name() -> Used in OOP - Name Mangling

# Perform some calculations
result1 = 10 + 5
print(result1)  # Output: 15


# Type Conversion - Changing the data type of a variable
# Implicit - Automatically done by the interpreter
print(10 + 20.5) # 30.5
print(10 + True) # 11
print("Hello" + 10) # Error - Cannot concatenate string with int

# Explicit - Done by the programmer
print("Hello" + str(10)) # Hello10
print(int(10.5)) # 10

print(int(3 + 4j)) # Error
print(str(3 + 4j)) # Able to convert - In fact anything is able to convert into string


# Literals - The value assigned to a variable / identifier
a = 0b1010 # Binary Literals - started with 0b or 0B
b = 100 # Decimal Literal 
c = 0o310 # Octal Literal - started with 0o or 0O
d = 0x12c # Hexadecimal Literal - started with 0x or 0X

print(d) # If you are going to print these values then it will print the human readable value

# Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

# Complex Literal  
x = 3.14j # Only j character is used along with any number
print(x, x.imag, x.real)

# String Literals
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923" # To represent emojis in python - unicode literals
raw_str = r"raw \n string" # you can include the escape sequence in the raw string - raw string literals

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# Demonstrating the print function's parameters:
# 'sep' parameter specifies the separator between the printed values
# 'end' parameter specifies what to print at the end of the statement
print("Hello Python", "Hello C++", sep=" seperator ", end="end")

# Print a new line
print("Second Line")

# Quick Quiz:
# The print function does not return any value (returns None), so
# 'a' will be assigned the value None. Then 'print(a)' will output None.
a = print(type(print(5)))  # Output: <class 'NoneType'>
print(a)  # Output: None


# Everything in Python is an object
a = 10  # an integer object
a = 5.875685  # reassigns 'a' to a float object
print(type(a))  # prints the type of 'a', which is now <class 'float'>

b = None  # 'None' is a special object representing the absence of value, of type 'NoneType'
print("The type of b is : ", type(b))  # prints the type of 'b', which is <class 'NoneType'>

print(type('python')) # prints the type of the string literal, which is <class 'str'>

c = [1, "dexter", {"age": 21}, 4.6]  # Lists are mutable
d = (1, "dexter", {"age": 21}, 4.6)  # Tuples are immutable

e = {
    "name": "Dexter",
    "college": "ABCD",
    'age': 69,
    True: "Whether redundant keys are possible to store in this",
    True: "Keys are in any form",
    None: 10
}  # Dictionary object with mixed keys, the second True key will overwrite the first one
print(type(e))  # Prints the type of 'e', which is <class 'dict'>
print(e[None])
print(e[True])  # Prints the value associated with the True key, which will be "Keys are in any form"

f = {'Hello', 'World', 'Welcome'}  # An unordered set object containing unique elements, order is not guaranteed
print(f)  # Prints the set 'f', order of elements may vary