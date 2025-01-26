# Namespace and Scope

# `Q1:` Write `Person` Class as given below and then display it's namespace.
"""
Class Name - Person

Attributes:
name - public
state - public
city - private
age - private

Methods:
address - public
It give address of the person as "<name>, <city>, <state>"
"""
# Write your code here
class Person:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.__city = None
        self.__age = None

    def get_city(self):
        return self.__city
    def set_city(self, city):
        self.__city = city

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def address(self):
        return f'{self.name}, {self.__city}, {self.state}'

for i in Person.__dict__: # Namespace of class
    print(i)

# Practice
def k():
    a = 0
    b = 0
    c = 0
    print(locals())

k.custom_attr = "Hey"
print(k.__dict__) # Returns custom_attr and not a, b, c because those are local variables will not accessiable outside the function scope - unlike class obj calling - function calling `print(k.a)` - returns an error

# `Q2:` Write a program to show namespace of object/instance of above(Person) class."""

p = Person("Dexter", "Maharashtra")

for i in p.__dict__: # Namespace of constructor
    print(i)


# `Q3:` Write a recursive program to calculate `gcd` and print no. of function calls taken to find the solution.
"""
gcd(5,10) -> result in 5 as gcd and function call 4
"""
def gcd(a, b):
    global call_count
    if b == 0:
        return a
    
    call_count += 1
    return gcd(b, a % b)

call_count = 0
gcd(97, 26)
print(call_count)


# Itterator And Generator

# `Q4:` Create MyEnumerate class,
"""
Create your own `MyEnumerate` class such that someone can use it instead of enumerate. It will need to return a `tuple` with each iteration, with the first element in the tuple being the `index` (starting with 0) and the second element being the `current element` from the underlying data structure. Trying to use `MyEnumerate` with a noniterable argument will result in an error.

```
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')
```

Output:
```
0 : a
1 : b
2 : c
```
"""
class MyEnumerate:
    def __init__(self, iterable: str):
        self.iterable = iterable
    
    def __iter__(self):
        return iterator(self)

class iterator:
    def __init__(self, obj: MyEnumerate):
        self.obj = obj
        self.start = 0
        self.end = len(self.obj.iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration("You reached the end")
        else:
            print(f"{self.start} : {self.obj.iterable[self.start]}")
            self.start += 1

obj = MyEnumerate("abc")
it = iter(obj)
next(it)
next(it)
next(it)
next(it)


# `Q5:` Iterate in circle
"""
Define a class, `Circle`, that takes two arguments when defined: a sequence and a number. The idea is that the object will then return elements the defined number of times. If the number is greater than the number of elements, then the sequence  repeats as necessary. You can define an another class used as a helper (like I call `CircleIterator`).

```
c = Circle('abc', 5)
d = Circle('abc', 7)
print(list(c))
print(list(d))
```

Output
```
[a, b, c, a, b]
[a, b, c, a, b, c, a]
```
"""
class MyEnumerate:
    def __init__(self, iterable: str, number: int):
        self.iterable = iterable
        self.number = number
        self.start = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.number:
            raise StopIteration("You reached the end")
        else:
            value = self.iterable[self.start % len(self.iterable)]
            self.start += 1
            return value

obj = MyEnumerate("abc", 5)
print(list(obj))


# `Q6:` Generator time elapsed
"""
Write a generator function whose argument must be iterable. With each iteration, the generator will return a two-element tuple. The first element in the tuple will be an integer indicating how many seconds have passed since the previous iteration. The tuple’s second element will be the next item from the passed argument.

Note that the timing should be relative to the previous iteration, not when the
generator was first created or invoked. Thus the timing number in the first iteration
will be 0

```
for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)
```

Output:
```
(0.0, 'a')
(2.005651817999933, 'b')
(2.0023095009998997, 'c')
(2.001949742000079, 'd')
```
Note: Your output may differ because of diffrent system has different processing configuration.
"""
import time
def elapsed_since(iterable):
    start = time.time()
    for i in iterable:
        yield f"{time.time() - start} : {i}"
        start = time.time()
        time.sleep(2)

iterable = 'abcde'
for i in elapsed_since(iterable):
    print(i)


# Decorators

# `Q7:` Write a Python program to make a chain of function decorators (bold, italic, underline etc.) on a given function which prints "hello world"
"""
```
def hello():
    return "hello world"
```

```
bold - wrap string with <b> tag. <b>Str</b>
italic - wrap string with <i> tag. <i>Str</i>
underline- wrap string with <u> tag. <u>Str</u>
```
"""

def bold(func):
    def inner():
        return "<b>" + func() + "</b>"
    return inner

def italic(func):
    def inner():
        return "<i>" + func() + "</i>"
    return inner

@bold
@italic
def hello():
    return "Hello World"

print(hello())


# `Q8:` Write a decorator called `printer` which causes any decorated function to print their return values. If the return value of a given function is `None`, printer should do nothing.

# Write your code here
from functools import wraps
def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return_value = func(*args, **kwargs)
        if return_value is not None:
            print(return_value)
        return return_value
    return inner

@printer
def hello(string):
    return string
hello("hello")


# `Q9:` Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.
"""
Lets say given function
def hello(string):
    print(string)

on calling after specified decorator is inplaced
hello('hello')
```

Output:
```
hello
hello
```
"""
def decorator(func):
    def inner(*args, **kwargs):
        print(func(*args, **kwargs))
        print(func(*args, **kwargs))
    return inner

@decorator
def func():
    return "Hello"

func()


"""### `Q10:` Write a decorator which doubles the return value of any function. And test that decoratos is working correctly or not using `asert`.

```
add(2,3) -> result in 10. Without decorator it should be 5.
```
"""
def double(func):
    def inner(*args):
        return 2 * func(*args)
    return inner

@double
def add(a, b):
    return a + b

a = 7
b = 8
assert (a + b) * 2 == add(a, b), "Values are not matching"
print("Values are matching")