# There are 2 stages where error may happen in a program
'''
- During compilation (Compile Time) -> Syntax Error
- During execution (Run Time) -> Exceptions
'''

# Syntax Error
'''
- Something in the program is not written according to the program grammar.
- Error is raised by the interpreter/compiler
- You can solve it by rectifying the program
'''

# Examples of syntax error
'''
print 'hello world'
'''

### Other examples of syntax error
'''
- Leaving symbols like colon,brackets
- Misspelling a keyword
- Incorrect indentation
- empty if/else/loops/class/functions
'''

'''
a = 5
if a==3
  print('hello')

a = 5
iff a==3:
  print('hello')

a = 5
if a==3:
print('hello')
'''

# IndexError - The IndexError is thrown when trying to access an item at an invalid index.
L = [1,2,3]
L[100]

# ModuleNotFoundError - The ModuleNotFoundError is thrown when a module could not be found.
import mathi
math.floor(5.3)

# KeyError - The KeyError is thrown when a key is not found
d = {'name':'nitish'}
d['age']

# TypeError - The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
1 + 'a'

# ValueError - The ValueError is thrown when a function's argument is of an inappropriate type.
int('a')

# NameError - The NameError is thrown when an object could not be found.
print(k)

# AttributeError - When a class does not have an attribute.
L = [1,2,3]
L.upper()

# Exceptions - logical errors
'''
If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.

- Exceptions are raised by python runtime
- You have to takle is on the fly
'''

# Examples
'''
- Memory overflow
- Divide by 0 -> logical error
- Database error
'''

# Why is it important to handle exceptions
# how to handle exceptions
# -> Try except block

# When you are communicating with external files you must be handele them in try except block

# let's create a file
with open('sample.txt','w') as f:
  f.write('hello world')

# try catch demo
try:
  with open('sample1.txt','r') as f:
    print(f.read())
except:
  print('sorry file not found')

# Getting the name if error
try:
  with open('sample123.txt','r') as f:
    print(f.read())
except Exception as e:
  print('The type of an exception is: ', e.with_traceback)
 
# catching specific exception
try:
  m=5
  f = open('sample1.txt','r')
  print(f.read())
  print(m)
  print(5/2)
  L = [1,2,3]
  L[100]
except FileNotFoundError:
  print('file not found')
except NameError:
  print('variable not defined')
except ZeroDivisionError:
  print("can't divide by 0")
except Exception as e:
  print(e)

# else
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else: # if try block is executed successfully
  print(f.read())

# finally
# else
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())
finally: # always executed whether exception is raised or not
  print('ye to print hoga hi') # closing the database connection or file connection or any other resource.

# raise Exception
# In Python programming, exceptions are raised when errors occur at runtime.
# We can also manually raise exceptions using the raise keyword.

# We can optionally pass values to the exception to clarify why that exception was raised

raise ZeroDivisionError('aise hi try kar raha hu')
# Java
# try -> try
# except -> catch
# raise -> throw

class Bank:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise Exception('amount cannot be -ve')
    if self.balance < amount:
      raise Exception('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
  obj.withdraw(15000)
except Exception as e:
  print(e)
else:
  print(obj.balance)

class MyException(Exception):
  def __init__(self,message):
    print(message)

class Bank:
  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise MyException('amount cannot be -ve')
    if self.balance < amount:
      raise MyException('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
  obj.withdraw(5000)
except MyException as e:
  pass
else:
  print(obj.balance)