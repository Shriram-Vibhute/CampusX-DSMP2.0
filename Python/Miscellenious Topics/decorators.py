# Decorators - Its literal meaning is to ‘decorate’ the function objects. To ‘decorate’ here means if you want to perform some extra functionality that supplements the original function, but isn’t necessarily part of the core logic of that function. A simple example is measuring the efficiency of a function using the time module


# Default Decorators
def outer(func): # This function `outer` is a decorator which is decorating the `inner` function
    def inner(): # This is the inner functions which is used to call the actual functions which is going to be decorated
        # Mentioning all sorts of things to decorate the function
        print('Modified Function')
        print(func()) # Calling the actual function
        return "ok" # OPTIONAL
    return inner # Here we returned the decorated function

# 1st way to call the function
@outer # Mentioning the decorator
def myfunc(): # Then defined the function that you want to decorate
    return "This function is doing something"
print(myfunc()) # Calling the function which return the decorated form


# 2nd Way to call the function - without decorator
print(outer(myfunc)()) # without decorating `@outer` this will run perfectly

# 3rd Way to call the function - without decorator
def outer(func):
    def inner():
        print('Modified Function')
        print(func())
        return "ok"
    return inner() # because the inner function is calling at this position
print(outer(myfunc)) # No need to call here


# Parameterized Decorator
def outer(func):
    def inner(a, b):
        print('The two numbers are -> ', a, b)
        return func(a, b)
    return inner

@outer
def myfunc(a, b):
    return (f'The sum is -> {a + b}')
print(myfunc(1, 2))

print(outer(myfunc)(1, 2))


# Logging Decorator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_function_call(func):
    def decorator(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorator

@log_function_call
def add(a, b):
    return a + b

# Call the decorated function
print(add(1, 2))


# Time require to run a function using `decoder`
import time
def outer(func):
    def inner(a: int=None, b: int=None) -> str:
        start = time.time()
        print(f"The sum is: {func(a, b)}")
        total_time = time.time() - start
        return f"Total time require to run this function is {total_time}"
    return inner

@outer
def myFunc(a: int=None, b: int=None) -> int:
    time.sleep(2)
    return int(a + b)

print(myFunc(a=10, b=20))


# TODO: Why and Where is the need of of the decorators
"""
The Why?
    "The primary need for Python decorators stems from a fundamental programming principle: Separation of Concerns and the desire for clean, reusable, and non-duplicative code."
    "In simpler terms, decorators allow us to add new behavior or modify the behavior of an existing function or class without permanently modifying its structure. They are a powerful application of Python's first-class functions."
    The problem they solve: Imagine you have multiple functions, and you want to add the same common feature to all of them—like logging, timing, or access control. Without decorators, you'd have to copy and paste the same boilerplate code into every single function. This is error-prone, violates the DRY (Don't Repeat Yourself) principle, and clutters the core logic of your functions.
"""

# Applications of Decoders
# 1. Logging & Instrumentation
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(5, 3) # Automatically logs the call and return value


# 2. Performance Measurement (Timing)
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return value
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function() # Prints: slow_function took 2.0052 seconds

# 3. Authentication & Authorization
def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_admin:
            raise PermissionError("Admin rights required")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_database(user):
    # Code to delete the database
    print("Database deleted!")

class User:
    def __init__(self, user_id: int=None, admin: bool=False) -> None:
        self.user_id=user_id
        if self.user_id < 10:
            self.is_admin = True

dex = User(user_id=1)
delete_database(dex)
# This will raise an error if user.is_admin is False

# 4. Input Validation & Sanitization
def validate_non_negative(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Arguments must be non-negative")
        return func(*args, **kwargs)
    return wrapper

@validate_non_negative
def calculate_area(length, width):
    return length * width

calculate_area(10, 20)
# calculate_area(-5, 10) # This would raise a ValueError