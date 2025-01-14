# instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class

class student:
    college = "PCCOE" # class variable shared by all instances - They mey not be unique
    branch = "Computer Science"

    def __init__(self, name, roll_no):
        self.name = name    # instance variable unique to each instance
        self.roll_no = roll_no

ms = student('dhoni', 7)
ro = student('rohit', 45)
virat = student('virat', 18)

print(ms.name, ro.name, virat.name)
print(ms.college, ro.college, virat.college)

# If you change the value of class_variables by any instance then the value will be changed for only that instences. 
ro.college = 'COEP'
print(ms.college, ro.college, virat.college)