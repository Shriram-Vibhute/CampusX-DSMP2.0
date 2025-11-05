def g(y):
  print(x)
  print(x+1)
x = 5
g(x)
print(x)

x = 5
def f(y):
    x = 1 # This is local
    x += 1
    print(x)
f(x)
print(x)

x = 5
def h(y):
    x += 1 # Error - You cannot do something like these inside a function without creating a local variable
h(x)
print(x)

def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x
x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

# Using global variables inside the functions
a = 10
def dummy(var):
  # a = 34 - you cannot initilize global var before golbal indication in funtion
  global a
  # a = 20 - you are updating the global value of a
  print(a)
dummy(10)

# You can access global variables into local scope but you cannot modify them until and unless you mention global keyword - But this is not a good practice because is could be possible that others functions also using those value

# The nonlocal keyword is used to work with variables in nested functions. It allows you to modify a variable defined in the nearest enclosing scope that isn't global.
def create_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
        
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    return increment, decrement

inc, dec = create_counter()
print(inc())  # 1
print(inc())  # 2
print(dec())  # 1