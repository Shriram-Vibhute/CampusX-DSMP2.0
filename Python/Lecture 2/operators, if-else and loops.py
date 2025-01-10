"""
Operators in Python
- Arithmetic Operators
- Relational Operators
- Logical Operators
- Bitwise Operators
- Assignment Operators
- Membership Operators
"""

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
print(~3)
print(4 >> 2)  # The newly introduced bits are dependent on the interpreter
print(5 << 2)  # The newly introduced bits are 0

# Assignment Operators
a = 2
a %= 2  # a = a % 2
print(a)

# Membership Operators
print('D' not in 'Delhi')
print(1 in [2, 3, 4, 5, 6])

# Program - Find the sum of a 3 digit number entered by the user
number = int(input('Enter a 3 digit number: '))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
print(a + b + c)

"""If-else in Python"""
# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input('Enter email: ')
password = input('Enter password: ')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'nitish.campusx@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('Enter password again: ')
  if password == '1234':
    print('Welcome, finally!')
  else:
    print('Maximum attempts reached')
else:
  print('Not correct')

# if-else examples
# 1. Find the min of 3 given numbers
# 2. Menu Driven Program

# min of 3 numbers

a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))

if a < b and a < c:
  print('Smallest is', a)
elif b < c:
  print('Smallest is', b)
else:
  print('Smallest is', c)

# menu driven calculator
menu = input("Hi! How can I help you? 1. Enter 1 for pin change 2. Enter 2 for balance check 3. Enter 3 for cash withdrawal 4. Enter 4 for exit: ")

if menu == '1':
  print('Pin change')
elif menu == '2':
  print('Balance check')
elif menu == '3':
  print('Cash withdrawal')
else:
  print('Exit')

"""Modules in Python
- math
- keywords
- random
- datetime
"""

# math
import math
math.sqrt(196)

# keyword
import keyword
print(keyword.kwlist) # Return all the keywords in python

# random
import random
print(random.randint(1,100))

# datetime
import datetime
print(datetime.datetime.now())

help('modules') # List of all the modules provided by python including the ones we have installed

"""Loops in Python
- Need of loops
- While Loop
- For Loop
"""

# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg

number = int(input('Enter the number: '))

i = 1

while i < 11:
  print(number, '*', i, '=', number * i)
  i += 1

# while loop with else

x = 1

while x < 3:
  print(x)
  x += 1

else:
  print('Limit crossed')

# Guessing game

# generate a random integer between 1 and 100
import random
jackpot = random.randint(1, 100)

guess = int(input('Guess the number: '))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print('Wrong! Guess higher')
  else:
    print('Wrong! Guess lower')

  guess = int(input('Guess again: '))
  counter += 1

else:
  print('Correct guess!')
  print('Attempts:', counter)

# For loop demo

for i in {1, 2, 3, 4, 5}:
  print(i)

# For loop examples

"""Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years."""

# Code Used in the session
curr_pop = 10000

for i in range(10, 0, -1):
  print(i, curr_pop)
  curr_pop = curr_pop - 0.1 * curr_pop # This is wrong as the population is increasing by 10% every year, if the population is decreasing then we can use this formula

# Correct Answer of above question:
curr_pop = 10000

for i in range(10, 0, -1):
  print(i, curr_pop)
  curr_pop /= 1.1