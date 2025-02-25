# `Q-1`: You are given a function definition. There might be several issues on execution of this function. You are asked to do exception handling for diffrent errors that this function goes in to `without altering this function`. And print error text.
"""
Function parameters `l -> list, s -> could be anything`

```
def function(l: list, s, **args):
    last_element = l[-1]
    
    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10
    
    res = sum(l)
    
    p = args['p']
    # print(p)
    return res/last_element * p + any_element

```
Check for different function calls:-

```
function([1,2,1], 12)
function([1,2,1]*9, '1-2')
function([1,'2',1]*9, 12)
function([1,'2',1]*9, 12)
function([1,2,0]*9, 12  )
function([1,2,1]*9, 12, p=None)
function([1,2,0]*9, 12, p=10)
```
"""
def function(l: list, s, **args):
    # 1st exception
    try:
        last_element = l[-1]
    except IndexError:
        print("IndexError - Index is out of range, The list is empty")
        last_element = 0
    
    # 2nd exception
    try:
        l[int(s)] = 10
    except ValueError:
        print("TypeError - s in not convertable to integer")
    except IndexError:
        print("IndexError - Index out of range")
    
    # 3rd exception
    try:
        any_element = l[int(s)+10]
    except ValueError:
        print("ValueError - s in not convertable to integer")
        any_element = 0
    except IndexError:
        print("IndexError - Index out of range")
        any_element = 0
    except TypeError:
        print("TypeError - string and number will not concatinated")
        any_element = 0
    
    # 4th Exception
    try:
        l[s] = 10
    except TypeError:
        print("TypeError - list indices must be integers or slices, not str")
    except IndexError:
        print("IndexError - Index out of range")
    
    # 5th Exception
    try:
        res = sum(l)
    except TypeError:
        print("TypeError - + is not able to work between string and numbers")
        res = 0
    
    # 6th Exception
    try:
        p = args['p']
    except KeyError:
        print("KeyError - key is not present")
        p = 0
    
    # 7th Exception
    try:
        return res/last_element * p + any_element
    except ZeroDivisionError:
        print("ZeroDivisionError - Zero Division Error")
        return 0
    except TypeError:
        print("TypeError - arathametic operations will not operated between string and numbers")

print(function([1,2,1], 12))
print(function([1,2,1]*9, '1-2'))
print(function([1,'2',1]*9, 12))
print(function([1,'2',1]*9, 12))
print(function([1,2,0]*9, 12))
print(function([1,2,1]*9, 12, p=None))
print(function([1,2,0]*9, 12, p=10))

"""###`Q-2:` You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of `sum of elements`.

List have elemnts as any no of  `key-pair dict with key as list index and value as any integer`, `integers` and `numeric-strings`. There is always only one element in the dict.


```
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])


print(s)
```
"""
l = [{0:2},2,3,4,'5', {5:10}]
s = 0
for i in range(len(l)):
    try:
        s += l[i].get(i)
    except KeyError:
        print("KeyError - The Key is not found in the dictonary")
        s = 0
    except AttributeError:
        print("AttributeError - The attribut get is not a part of datatype")
        try:
            s += l[i]
        except TypeError:
            print("TypeError - str + number")
            s += int(l[i])

print(s)

# `Q-3:`: File Handling with Exception handling
"""
Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).
"""
try:
    with open("sample.txt", 'w') as f:
        f.write("Hello, Good Morning!!!")
except Exception as e:
    print("some exception occured")
else:
    print("File writing successifully")

# `Q-4`: Number game program.
"""
Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a **ValueTooLarge** exception. If the value is smaller the number to be guessed the, raise a **ValueTooSmall** exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise **GuessError** if user guess a number less than 1.
"""
class ValueTooLarge(Exception):
    def __init__(self, *message):
        print(message)

class ValueTooSmall(Exception):
    def __init__(self, *message):
        print(message)

class GuessError(Exception):
    def __init__(self, *message):
        print(message)

real = 10
while True:
    try:
        your_guess = int(input("Guess the number : "))
        if your_guess < 1:
            raise GuessError("Number is less than 1")
        elif your_guess < real:
            raise ValueTooSmall("The real number is greated than the number you guessed")
        elif your_guess > real:
            raise ValueTooLarge("The real number is smaller than the number you guessed")
        else:
            print("Congrulation, you guessed it correct")
            break
    except ValueTooSmall as e:
        print("Next Try")
    except ValueTooLarge as e:
        print("Next Try")
    except GuessError as e:
        print("Next Try")


# `Q-6`: Write a python function which infinitely prints natural numbers in a single line. Raise the **StopIteration** exception after displaying first 20 numnbers to exit from the program."""
i = 0
while True:
    print(i, end = "")
    try:
        i += 1
        if i == 20:
            raise StopIteration()
    except StopIteration:
        print("StopIteration error")
        break