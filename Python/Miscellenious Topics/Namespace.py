# Namespaces
"""
A namespace is a space that holds names(identifiers). Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values)

There are 4 types of namespaces:
- Builtin Namespace
- Global Namespace
- Enclosing Namespace
- Local Namespace

# Scope and LEGB Rule - Precedance of namespaces from `local` to `built-in`

A scope is a textual region of a Python program where a namespace is directly accessible.

The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope. If the interpreter doesn't find the name in any of these locations, then Python raises a NameError exception.
"""

def k():
    a = 10 
    # global a - SyntaxError: name 'a' is assigned before global declaration
    a = 34
    print(a)

l = [1,2,3]
print(min(l)) 
def min(): # Overriding built-in namespace function
    print("Hey")
min()

a = 45
def update_global():
    # a += 1 # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    a = 10
    a += 45
    # First you have to declare and define the variable and then update inplace as per requirement
    print(a)

update_global()

# Creating global variable inside local namespace and accessing at global namespace
def global_var_inside_local():
    # local var
    global a
    a = 1
    print(a)

global_var_inside_local()
print(a)

# built-in namespace
import builtins
print(dir(builtins))

# `nonlocal` namespace - The variables inside the parent function will be accesse through `nonlocal` keyward inside its child functions
a = 45
def outer():
    b = 100
    def inner():
        global a
        nonlocal b
        return a + b
    return inner()

print(outer())

# Note that you can declare global variables from local namespaces but you cannot declare nonlocal variables from local instances
def outer():
    def inner():
        global a
        # nonlocal b - Error
        return a + b
    return inner()

a = 10
def grand_parent():
    a = 100
    def parent():
        nonlocal a
        def son():
            nonlocal a # It will access 100 because in parent() accessing `a` from grand_parent()
            print(a)
        son()
    parent()
grand_parent()