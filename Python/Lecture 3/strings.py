''' 
In Python, strings are a sequence of "Unicode Characters".

Why Unicode? ASCII supports 8-bit characters which is very small and can only support 256 characters. Unicode supports 16-bit characters which can support emojis and 4.3 billion characters.

- Creating Strings
- Accessing Strings
- Adding Chars to Strings
- Editing Strings
- Deleting Strings
- Operations on Strings
- String Functions
'''

# Creating Strings
s = 'hello'
s = "hello"
s = '''hello'''
s = """hello"""
s = str('hello')
print(s)

# Accessing Substrings from a String
# Positive Indexing
s = 'hello world'
# print(s[41]) # Error - Index out of range

# Negative Indexing
print(s[-3])

# Slicing
print(s[6:0:-2])

# Reversing
print(s[::-1])

# Reverse Iteration
print(s[-1:-6:-1])

# Editing and Deleting in Strings
# s[0] = 'H' # Error - Strings are immutable
# del s[-1:-5:2] # Error - Strings are immutable

# Operations on Strings
print('delhi' + ' ' + 'mumbai')
print('delhi'*5)
print("*"*50)
print('delhi' != 'delhi')
print('mumbai' < 'mumbb') # Lexicographical(Letter by letter) Comparison
print('Pune' > 'pune')

print('hello' and 'world') # Returns the second value if first is True
print('hello' or 'world') # Returns the first value if first is True
print('' and 'world') # Returns the first value if first is False
print('' or False) # Returns the second value if first is False
print(not 'hello')

for i in 'hello':
  print(i)

for i in 'delhi':
  print('pune')

# Membership Operations
print('D' in 'delhi')

# Common Functions
print(len('hello world'))
print(max('hello world'))
print(min('hello world'))
print(sorted('hello world', reverse=True))

# Capitalize/Title/Upper/Lower/Swapcase
s = 'hello world'
print(s.capitalize())
print(s.title())
print(s.upper())
print('Hello World'.lower())
print('HeLlO WorLD'.swapcase())

# Count/Find/Index
print('my name is Rocky'.count('i'))
print('my name is Rocky'.find('x'))
# print('my name is Rocky'.index('x')) # will return error if not found

# endswith/startswith
print('my name is Rocky'.endswith('sho'))
print('my name is Rocky'.startswith('1my'))

# format
name = 'Rocky'
gender = 'male'
print('Hi my name is {1} and I am a {0}'.format(gender, name))

# isalnum/ isalpha/ isdigit/ isidentifier
print('Rocky1234%'.isalnum())
print('Rocky'.isalpha())
print('123abc'.isdigit())
print('first-name'.isidentifier())

# Split/Join
print('hi my name is Rocky'.split())
print(" ".join(['hi', 'my', 'name', 'is', 'Rocky']))

# Replace
print('hi my name is Rocky, Rocky'.replace('Rocky', 'Sam')) # Replace all the occurrences

# Strip
print('Rocky                           '.strip())

# String Questions

# Find the length of a given string without using the len() function
s = input('Enter the string: ')
counter = 0
for i in s:
  counter += 1
print('Length of string is', counter)

# Extract username from a given email
s = input('Enter the email: ')
pos = s.index('@')
print('Username:', s[0:pos])

# Count the frequency of a particular character in a provided string
s = input('Enter the string: ')
term = input('What would you like to search for: ')
counter = 0
for i in s:
  if i == term:
    counter += 1
print('Frequency:', counter)

# Remove a particular character from a string
s = input('Enter the string: ')
term = input('What would you like to remove: ')
result = ''
for i in s:
  if i != term:
    result += i
print('Result:', result)

# Check whether a given string is palindrome or not
s = input('Enter the string: ')
flag = True
for i in range(0, len(s) // 2):
  if s[i] != s[len(s) - i - 1]:
    flag = False
    print('Not a Palindrome')
    break
if flag:
  print('Palindrome')

# Count the number of words in a string without split()
s = input('Enter the string: ')
L = []
temp = ''
for i in s:
  if i != ' ':
    temp += i
  else:
    L.append(temp)
    temp = ''
L.append(temp)
print('Words:', L)

# Convert a string to title case without using the title()
s = input('Enter the string: ')
L = []
for i in s.split():
  L.append(i[0].upper() + i[1:].lower())
print('Title Case:', " ".join(L))

# Convert an integer to string
number = int(input('Enter the number: '))
digits = '0123456789'
result = ''
while number != 0:
  result = digits[number % 10] + result
  number = number // 10
print('String:', result)
print('Type:', type(result))