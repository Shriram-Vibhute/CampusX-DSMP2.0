class marathon:
    race_number = 0
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.race_count()
    
    @staticmethod
    def race_count():
        marathon.race_number += 1

print(marathon.race_number)
t1 = marathon('t1', 1)
t2 = marathon('t2', 2)
t3 = marathon('t3', 3)
t4 = marathon('t4', 4)
t5 = marathon('t5', 5)

# marathon.race_count()
print(marathon.race_number)
t6 = marathon('t6', 6)
t7 = marathon('t7', 7)
t8 = marathon('t8', 8)
t8.race_count()
t8.race_count() # You can call them using objects as well
# Everytime you create a new object the static method will get automatically triggred

# marathon.race_count()
print(marathon.race_number)