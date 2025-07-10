class student:
    college = 'PCCOE'
    branch = 'Computer Science'

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    
    @classmethod # Class Method
    def altConstructor(class_name, info, age_info) -> None:
        # Direct access of class method
        class_name.college = 'COEP'
        class_name.branch = 'IT'

        # Indirect access of instance variables
        name = info.split("-")[0]
        id = int(info.split("-")[1])
        age = age_info
        return class_name(name, id, age) # Creating a new instance by calling a constructor
    
    def print_data(self): # Instance Method
        print(self.name, self.age, self.branch)

s1 = student("jonny", 17, 100)
s2 = student.altConstructor("jack-12", 20)
s3 = s2.altConstructor("Mark-12", 20)
student.branch = "ABC" # This will work

print(f"name: {s2.name} | id: {s2.id} | age: {s2.age}")
s2.print_data()

'''
@classmethod (Class Methods)
Definition: A @classmethod is a method that is bound to the class rather than its instances. It takes cls as its first parameter, which refers to the class itself.

Usage: @classmethod is often used for factory methods that need to access or modify class-level data or perform operations related to the class rather than a specific instance.

Access: It can access class variables and other class methods. It cannot access instance variables or instance methods directly.

def Method (Instance Method)
Definition: An instance method is a method that is bound to an instance of the class. It takes self as its first parameter, which refers to the instance of the class.

Usage: Instance methods are used to access or modify instance-specific data and perform operations that are related to the particular instance.

Access: It can access both instance variables and class variables. It can also call other instance methods.
'''

# Difference between @classmethod and @staticmethod
class Example:
    count = 0  # Class variable

    def __init__(self, value):
        self.value = value  # Instance variable

    @classmethod
    def increment_count(cls):
        cls.count += 1
        print(f"Count incremented to {cls.count}")

    @staticmethod
    def utility_method(param):
        print(f"Utility method called with {param}")

# Using the class method
Example.increment_count()  # Outputs: Count incremented to 1

# Using the static method
Example.utility_method("test")  # Outputs: Utility method called with test