# Default Decorators
def outer(func):
    def inner():
        print('Modified Function')
        print(func())
        return "ok"
    return inner

# 1st way to call the function
@outer
def myfunc():
    return "This function is doing something"
print(myfunc())

# 2nd Way to call the function
print(outer(myfunc)())

# 3rd Way to call the function
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
        func(a, b)
        return a + b
    return inner

@outer
def myfunc(a, b):
    print('The sum is -> ')
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

'''
You cannot do like this
print("Inside the inner function")
print(func_inner())
return new_func
-> Then this function is not a decorator anymore
'''