# Discrete Data Types / Data Structures
print("Number - ", 1e308)
print("Null - ", None) # Does not return anything

print("String - ", "Hello World")
print("Symbol - ", 1+2j)

print("Boolean - ", True)
print("BigInt - ")

print("undefined - ", None) # Not yet assigned

# Collection Data-Types / Data-Structures
print("List - ", [1, 2, 3, 4, 5])
print("Tuple - ", (1, 2, 3, 4, 5))
print("Dictionary - ", {"Name": "John", "Age": 30})
print("Set - ", {1, 2, 3, 4, 5})

# type function
print(type(1e308))

# Dynamic Typing - Automatically detect the data type
name = 'Dexter Morgan'
age = 30 

# Dynamic Binding - Change the datatype at runtime
name = "Dexter Morgan"
print(name)
name = 30
print(name)

# Interview Questions - What is the difference between Static/Dynamic Typing and Static/Dynamic Binding?

# Multiple Assignment shorthand
a, b, c = 1, 2, 3
c = d = e = 100

# Identifiers - Naming Conventions - Basically a name given to a variable, function, class, etc.
_ = 10 # Used in Temporary or insignificant variable and Interpreter variable
__ = 20 # Used in OOP - Name Mangling

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

# Differencing between "Type Conversion" and "Type Casting" - Type Conversion is done by the programmer and Type Casting is done by the interpreter

# Literals - The value assigned to a variable / identifier
a = 0b1010 # Binary Literals - started with 0b or 0B
b = 100 # Decimal Literal 
c = 0o310 # Octal Literal - started with 0o or 0O
d = 0x12c # Hexadecimal Literal - started with 0x or 0X

print(a) # If you are going to print these values then it will print the human readable value

# Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2 -> Scientific Notation
float_3 = 1.5e-3 # 1.5 * 10^-3

# Complex Literal 
x = 3.14j
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