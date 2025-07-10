class student:
    # You cannot define multiple __init__ methods with different parameters in a single class - the last definition will overwrite the previous ones.
    '''
    def __init__(self) -> None:
        print("This is Non-Parameterized constructor")
    '''
    # Parameterized Constructor
    def __init__(self, name, id, branch) -> None:
        self.name = name; self.id = id; self.branch = branch

    # You can do something like this - it works without an error but introduce unnecessary ambiguity
    '''
    def __init__(self, param) -> None:
        pass

    def __init__(self, param) -> None:
        pass
    ''' 
    # Custom Constructor
    @classmethod
    def custom_cust(class_name, combined_string: str):
        # combined_string = 'harry-20-IT'
        name, id, branch = combined_string.split('-')
        return class_name(name, id, branch)
    
    @classmethod
    def custom_cust_2(class_name, combined_string: str):
        name, id, branch = combined_string.split('|')
        return class_name(name, id, branch)

rohit = student()
yash = student('yash', 12, 'CS')
harry = student.custom_cust('harry-20-IT')
bharat = student.custom_cust_2('bharat|89|Mech')

print(yash.name, yash.id, yash.branch)
print(harry.name, harry.id, harry.branch)
print(bharat.name, bharat.id, bharat.branch)

# Default Constructor - When we do not include the constructor in the class or forget to declare it, then that becomes the default constructor. It does not perform any task but initializes the objects.
class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()  

# Note: The constructor overloading is not allowed in Python.