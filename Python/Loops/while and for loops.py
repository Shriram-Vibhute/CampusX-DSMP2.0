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

for i in {1, 2, 3, 4, 5}: # Sets are unordered but you can still iterate over them.
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


# Sequence sum 1/1! + 2/2! + 3/3! + .. 
n = int(input("Enter the number of terms : "))
denominator = 1
ans = 0
for i in range(1, n + 1):
  denominator *= i
  ans += i / denominator
print(ans)

# Nested Loops - Pattern Problems - 1
rows = int(input('enter number of rows : '))
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print('*', end = '')
  print()

# Pattern Problem - 2
rows = int(input('enter number of rows'))
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print(j, end = '')
  for j in range(i - 1, 0, -1):
    print(j, end = '')
  print()

# Loop Control Statement
'''
- Break
- Continue
- Pass
'''
for i in range(1,10):
  if i == 5:
    break
  print(i)

lower = int(input('enter lower range'))
upper = int(input('enter upper range'))
for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j == 0:
      break
  else:
    print(i)

for i in range(1,10):
  if i == 5:
    continue
  print(i)

for i in range(1,10):
  pass # This is actually used if you want to write a block of code but you don't want to write anything in it.