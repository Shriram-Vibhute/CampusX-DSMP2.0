class Student:
    def __init__(self, name, id, branch):
        self.name = name
        self.id = id
        self.branch = branch

    def print_(self):
        print(self.name, self.id, self.branch)

class Boys(Student):
    def __init__(self, name, id, branch):
        # print(task)
        super().__init__(name, id, branch)
    
    def print_(self):
        super().print_()

class Girls(Student):
    def __init__(self, name, id, branch):
        # print(task)
        super().__init__(name, id, branch)
    
    def print_(self):
        super().print_()

class Batch(Boys, Girls):
    def __init__(self, name, id, branch, batch):
        # To correctly initialize, ensure super() handles the call chain
        super().__init__(name, id, branch)
        Girls.__init__(self, name, id, branch)
        self.batch = batch
    
    def print_(self):
        # Use super().print() to follow the correct MRO
        super().print_()
        Girls.print_(self)
        # Local    
        print(self.batch)

# Creating an instance of Batch
b1 = Batch('Payal', '10', 'CS-AIML', 1)
b1.print_()

b2 = Batch('Prem', '45', 'IT', 2)
b2.print_()