class student:
    # Default Constructor
    def __init__(self, name, id, branch) -> None:
        self.name = name; self.id = id; self.branch = branch
    
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

yash = student('yash', 12, 'CS')
harry = student.custom_cust('harry-20-IT')
bharat = student.custom_cust_2('bharat|89|Mech')

print(yash.name, yash.id, yash.branch)
print(harry.name, harry.id, harry.branch)
print(bharat.name, bharat.id, bharat.branch)