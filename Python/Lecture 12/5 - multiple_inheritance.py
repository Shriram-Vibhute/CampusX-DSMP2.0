# Code is not running properly
class Animal:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
    def display(self):
        print("Animal - ", self.name, self.id)

class Dog(Animal):
    def __init__(self, name, id, temp = 0) -> None:
        super().__init__(name, id)
        self.temp = temp
    def display(self):
        super().display()
        print("Dog - ",self.temp)

class Cat(Animal):
    def __init__(self, name, id, temp = 0) -> None:
        super().__init__(name, id)
        self.temp = temp
    def display(self):
        super().display()
        print("Cat - ",self.temp)

class Sound(Cat, Dog):
    def __init__(self, name, id, temp) -> None:
        super().__init__(name, id, temp)
        Dog.__init__(self, name, id, temp) # This will be set as the values of base class as it executed after constructor of boy class
    
    def display(self):
        Cat.display(self)
        Dog.display(self)

s = Sound('Hi', 1, 10)
s.display()
# print('print options ->', s.name, s.id)