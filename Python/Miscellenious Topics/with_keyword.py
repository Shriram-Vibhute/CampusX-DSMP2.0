# Creating custon context mnagers

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        # Any setup actions can be performed here
        return self
    
    # Constructor
    def __init__(self, name, id):
        self.id = id
        print(name, id)
    
    # Getters and Setters
    @property
    def getter(self):
        return self.id
    @getter.setter
    def getter(self, val):
        return val + 10

    def __exit__(self, exc_type, exc_value, traceback):
        raise SyntaxError("SyntexError")
        print("Exiting the context")
        # Any teardown actions can be performed here
        # The exception details are passed to the arguments if an exception occurs

# Using the custom context manager
try:
    with MyContextManager('dex', 19) as cm:
        print("Inside the context")
        # Getters and setters
        print(cm.getter)
except SyntaxError as serror:
    print('Resolved')
    # Exiting the context automatically after the block