class Student:    
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age   
        self.__private = 45
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    
s = Student("John",101,22)    
print(s.__doc__) # Returns the doc string
print(s.__dict__) # Returns all the public and private attribute values in dict format
print(s.__module__) # Returns the module

class dex(Student):
    def __init__(self, name, id, age, branch):
        super().__init__(name, id, age)
        self.branch = branch

print(dex.__bases__)
# __bases__ -> It contains a tuple including all base classes.