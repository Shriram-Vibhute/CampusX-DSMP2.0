# Implicit Type Conversion
a = 1.9  # float
b = 8    # integer

print(a + b)  # implicit type casting: the integer 'b' is converted to a float to perform addition, result is a float

c = 'Dexter'  # string
d = True      # boolean

# print(c + d)  # Uncommenting this would raise an error because you cannot concatenate a string with a boolean directly
# Explicit TypeCasting
print(c + str(d))  # converts boolean 'd' to string and concatenates with 'c', result is 'DexterTrue'

# Explicit TypeCasting Examples

# Converting different types to string
num = 123  # integer
flt = 3.14  # float
bool_val = False  # boolean

# Convert to string explicitly
print(str(num))      # '123'
print(str(flt))      # '3.14'
print(str(bool_val)) # 'False'

# Converting string to other types
num_str = '456'  # numeric string
flt_str = '7.89'  # float string
bool_str = 'True'  # boolean string

# Convert to integer explicitly
print(int(num_str))  # 456

# Convert to float explicitly
print(float(flt_str))  # 7.89

# Convert to boolean explicitly
print(bool(bool_str))  # True; non-empty strings are considered True

# Note: Conversion from string to boolean requires specific handling, such as checking for 'True' or 'False' explicitly.

print(bool('False')) # If any type of content is present in string (even False) it will typecast it to true. In contrast if the string is false then it will typecast it to false

# Additional conversions:
# Converting a boolean to integer
bool_val = True
print(int(bool_val))  # 1

# Converting a boolean to float
print(float(bool_val))  # 1.0

# Converting an integer to boolean
print(bool(0))  # False; zero is considered False
print(bool(1))  # True; non-zero integers are considered True

# Converting a float to integer (will truncate the decimal part)
flt_val = 5.99
print(int(flt_val))  # 5

# Converting a float to boolean
print(bool(flt_val))  # True; non-zero floats are considered True

# Converting None to str
print(type(str(None))) 

# Convert list to dict
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
print(dict[str, int](list_of_tuples))  # {'a': 1, 'b': 2, 'c': 3}

# Convert dict to list
d = {'a': 1, 'b': 2, 'c': 3}
print(list(d.items()))  # [('a', 1), ('b', 2), ('c', 3)]