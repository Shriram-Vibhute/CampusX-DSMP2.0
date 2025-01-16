# Discrete Data Types / Data Structures
print("Number - ", 1e308)
print("Null - ", None) # Does not return anything

print("String - ", "Hello World")
print("Complex - ", 1+2j) 

print("Boolean - ", True)
print("BigInt - ")

print("undefined - ", None) # Not yet assigned

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

# Interview Questions - What is the difference between Static/Dynamic Typing and Static/Dynamic Binding?
'''
Actually, Dynamic Binding is a method resolution at runtime concept in OOPs - Which method has to get executed will be determined at runtime (Method overriding - Polymorphsm). This is also called "Late Binding"
'''

# Compile time vs Runtime
'''
Compile Time: The phase when the code is being written
Run Time: The phase when the compiled code is executed
'''

# Multiple Assignment shorthand
a, b, c = 1, 2, 3
c = d = e = 100

# Identifiers - Naming Conventions - Basically a name given to a variable, function, class, etc.
_ = 10 # Used in Temporary or insignificant variable and Interpreter variable
__ = 20 # Used in OOP - Name Mangling

# Perform some calculations
result1 = 10 + 5
print(result1)  # Output: 15

# The value of the last expression can be accessed using _
print(_)  # Output: 15
# Throwing an error of _ is not defined

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

# Differencing between "Type Conversion" and "Type Casting"
'''
- Type Casting - This is the process of explicitly changing a variable from one datatype to another
int('5')
- Type Conversion - Type conversion involves changing a variable from one data type to another, which can occur either implicitly or explicitly.
a = 5 + 6.09 = 11.09 -> Int to Float
'''

# Literals - The value assigned to a variable / identifier
a = 0b1010 # Binary Literals - started with 0b or 0B
b = 100 # Decimal Literal 
c = 0o310 # Octal Literal - started with 0o or 0O
d = 0x12c # Hexadecimal Literal - started with 0x or 0X

print(d) # If you are going to print these values then it will print the human readable value

# Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2 -> Scientific Notation
float_3 = 1.5e-3 # 1.5 * 10^-3

# Complex Literal  
x = 3.14j # Only j character is used along with any number
print(x, x.imag, x.real)

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

# The purpose of "None" apart from null representation - Variable Declaration
a = None 
b = None

# My Code

# Print a simple greeting message
print("hello world")

# Define a variable with value 56
a = 56

# Print the result of adding 45 to the variable 'a'
print(a + 45)

# You can multiply string with number
print('5' * 5)

# Uncommenting the following lines will cause errors due to type mismatch:
# Concatenation of string with an integer (not allowed)
# print("Shriram" + 56)  # This will raise a TypeError

# Adding a string and an integer (not allowed)
# b = "shriram" + 13  # This will also raise a TypeError

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