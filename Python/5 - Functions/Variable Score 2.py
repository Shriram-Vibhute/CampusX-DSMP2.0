def scope_test():
    def do_local():
        spam = "local spam"
        # This spam will only limited to do_local()

    def do_nonlocal():
        nonlocal spam # This spam will change the value of spam inside scope_test()
        spam = "nonlocal spam"

    def do_global():
        global spam # This spam will change the spam variable present at global
        spam = "global spam"

    spam = "test spam"

    do_local()
    print("After local assignment:", spam)
    # Local Scope:
    # do_local() defines a local variable spam inside its own function scope. This local variable spam does not affect the spam variable in scope_test().

    do_nonlocal()
    print("After nonlocal assignment:", spam)
    # Enclosing Scope:
    # do_nonlocal() modifies a variable in the enclosing scope (i.e., the spam variable in the scope_test() function). The nonlocal keyword allows do_nonlocal() to change the spam variable that was defined in scope_test(), not a new local variable.

    do_global()
    print("After global assignment:", spam)
    # Global Scope:
    # do_global() uses the global keyword to modify the spam variable in the global scope, meaning it will affect the spam variable defined outside of the scope_test() function.

scope_test()
print("In global scope:", spam) # Value will be changed due to do_global function
# We did not explicitely mentioned spam in global score. Since in the function global variable is mentioned which creats the variable if not possible and chenge the value - This is only possible with global and not with nonlocal


# Note -> nonlocal only work when it find the existance of nonlocal variable and not as global variable. 
'''
spam = None
def update():
    nonlocal spam
    spam = 'spam'
'''

def temp():
    global a
    a = 10
temp()
print(a)