# Creating custon context mnagers
class MyContextManager:
    def __enter__(self):
        # Here you menation all the variables and call the methods require to run this context manager 
        print("Entering the context")
        # Variables and Methods
        return self
    
    def __init__(self, name, id):
        self.id = id
        print(name, id)
    
    @property
    def getter(self):
        return self.id
    @getter.setter
    def getter(self, val):
        return val + 10

    def __exit__(self, exc_type, exc_value, traceback):
        # Here you do stuff like closing the db connection (teardown actions) and more 
        print("Exiting the context")
        # The exception details are passed to the arguments if an exception occurs

# Using the custom context manager
try:
    with MyContextManager('dex', 19) as cm:
        print("Inside the context")
        print(cm.getter)
except SyntaxError as serror:
    print('Resolved')
    # Exiting the context automatically after the block


class main:
    def __enter__(self):
        return self
    def __init__(self) -> None:
        print("This is main class")
    def sum(self, a, b):
        return a + b
    def __exit__(self, exc_type, exc_value, traceback): # `exc_type, exc_value, traceback` - maindatory
        pass

with main() as obj:
    print(obj.sum(a:=int(input("first number: ")), b:=int(input("sencod number: "))))

# If a class wants to works as a context class then it must contains the `enter and exit`` magic methods