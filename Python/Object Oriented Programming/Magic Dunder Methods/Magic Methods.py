class Student:
    def __init__(self, name):
        # Initializes the instance with a 'name' attribute
        self.name = name
    
    def __len__(self):
        # Returns the length of the 'name' attribute
        return len(self.name)
    
    def __str__(self):
        # Defines a human-readable string representation of the object
        return f"Student Name: {self.name}"
    
    def __repr__(self):
        # Defines the official string representation of the object
        # Ideally, this should be an expression that can recreate the object
        return f"Student(name='{self.name}')"
    
    def __call__(self):
        # Allows the instance to be called like a function
        return f"{self.name} is a student"

    def __eq__(self, other):
        # Defines behavior for equality comparison using '=='
        if isinstance(other, Student):
            return self.name == other.name
        return False
    
    def __lt__(self, other):
        # Defines behavior for less-than comparison using '<'
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __add__(self, other):
        # Defines behavior for addition using '+'
        if isinstance(other, Student):
            return Student(name=self.name + " & " + other.name)
        return NotImplemented

    def __getitem__(self, index):
        # Defines behavior for indexing (e.g., s[index])
        return self.name[index]
    
    def __contains__(self, substring):
        # Defines behavior for 'in' operator
        return substring in self.name

# Create instances of the Student class
s1 = Student('Alice')
s2 = Student('Bob')

# Use __len__ with len() function
print(len(s1))  # Output: 5

# Use __str__ with print() and str() function
print(str(s1))  # Output: Student Name: Alice
print(s1) # Output: Student Name: Alice (print implicitly calls __str__)

# Use __repr__ with repr() function - Returns a called object with its variable values
print(repr(s1))  # Output: Student(name='Alice')

# Use __call__ to call the instance like a function
print(s1())  # Output: Alice is a student

# Use __eq__ to compare two Student instances
print(s1 == s2)  # Output: False

# Use __lt__ for less-than comparison
print(s1 < s2)  # Output: False (based on lexicographical order of names)

# Use __add__ to concatenate names of two Student instances
s3 = s1 + s2
print(repr(s3))  # Output: Student(name='Alice & Bob')

# Use __getitem__ to access characters by index
print(s1[1])  # Output: l (second character of 'Alice')

# Use __contains__ to check for substring presence
print('Al' in s1)  # Output: True