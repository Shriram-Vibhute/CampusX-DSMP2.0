class Student:
    college = 'PCCOE'
    District = 'Pune'

    def __init__(self, name, id, branch):
        self.name = name
        self.id = id
        self.branch = branch
    
    @classmethod
    def cust_constructor(class_name, string):
        name, id, branch = string.split('-')
        return Student(name, id, branch)
    
    def print(self):
        print(self.name, self.id, self.branch)

class Boys(Student):
    def __init__(self, name, id, branch, sports):
        super().__init__(name, id, branch)
        self.sports = sports
    
    def print(self):
        if 0:
            super().print()
        else:
            print(self.sports)

Yash = Boys('yash', 12, 'CS', 'cricket')
Yash.print()