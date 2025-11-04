## Name Mangling in OOP

Name mangling is a mechanism in Python that helps with **encapsulation** in object-oriented programming. It's directly related to the double underscore (`__`) prefix.

### What is Name Mangling?

Name mangling is the process where Python automatically rewrites attribute names that start with double underscores (`__`) to include the class name, making them harder to accidentally override in subclasses.

### How it Works:

When you define an attribute with `__` prefix (like `__private_var`), Python automatically changes it to `_ClassName__private_var`.

### Example:
        
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

# WARNING: while using `=` operator between multiple identifiers, the address of the data is shared and not the value so if you assign a collection datastructure, the changes that you make with one identifier will reflect in all other identifiers.
a = b = c = []
b.append(10)
print(a, b, c)

c.append(20)
print(a, b, c)
# But this is not the case with discrete data types
a = b = c = 10
b = 20
print(a, b, c)

# Identifiers - Naming Conventions - Basically a name given to a variable, function, class, etc.
_ = 10 # Used in Temporary or insignificant variable and Interpreter variable
# __function_name() -> OOPs interview question - Name Mangling

# Name Mangling Example
class MyClass:
    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected"  # Convention for protected
        self.__private_var = "private"     # Name mangling applied
    
    def __private_method(self):
        return "This is private"
    
    def show_mangled_names(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private (mangled): {self.__private_var}")
        print(f"Private method (mangled): {self.__private_method()}")
        print(f"Actual mangled name: {self._MyClass__private_var}")

# Create instance
obj = MyClass()
obj.show_mangled_names()

# Try accessing from outside
print("\nAccessing from outside:")
print(f"Public: {obj.public_var}")          # Works
print(f"Protected: {obj._protected_var}")   # Works (but convention says don't)
# print(f"Private: {obj.__private_var}")     # Error: AttributeError
print(f"Mangled access: {obj._MyClass__private_var}")  # Works but should be avoided

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
          
I've added a practical example to your file that demonstrates name mangling. Here's what name mangling is all about:

## Key Points about Name Mangling:

1. **Purpose**: Prevents accidental overriding of "private" attributes in subclasses
2. **Syntax**: Attributes starting with `__` (but not ending with `__`) get mangled
3. **Mechanism**: Python rewrites `__private` to `_ClassName__private`
4. **Not truly private**: It's a convention, not enforced privacy (you can still access via mangled name)

### What gets mangled:
- `__variable` → becomes `_ClassName__variable`
- `__method()` → becomes `_ClassName__method()`

### What doesn't get mangled:
- `__init__` (magic methods)
- `__str__` (magic methods)  
- `__variable__` (names with double underscores at both ends)

### Why use it?
- **Encapsulation**: Helps prevent accidental name clashes in inheritance
- **Code organization**: Clearly indicates intended "private" members
- **Interview question**: Common OOP concept asked in Python interviews

The example I added shows how public, protected (single underscore convention), and private (double underscore with name mangling) attributes behave differently when accessed from outside the class.