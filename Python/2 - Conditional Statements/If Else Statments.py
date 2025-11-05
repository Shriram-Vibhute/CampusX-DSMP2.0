# if elif else ladder
i = 25
if (i == 10):
  print("i is 10")
elif (i == 15):
  print("i is 15")
elif (i == 20):
  print("i is 20")
else:
  print("i is not present")

# Nested If statement
i = 10
if (i == 10):
  if (i < 15):
    print("i is smaller than 15")
  if (i < 12):
    print("i is smaller than 12 too")
  else:
    print("i is greater than 15")

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