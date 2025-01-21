# `Q1:`Count number of instances of a class created in Python?
"""
Example:
Say `Car` is any class.
```
maruti = Car()
bmw = Car()
honda = Car()
```
So after creating above instances. We want to count how many instances are created of Car class.

For above example `no of instances = 3`.

Write a program for above problem.
"""
class Car:
    # Defining class variable
    __counter = 0

    def __init__(self):
        Car.increaseCounter()
    
    @staticmethod
    def increaseCounter():
        Car.__counter += 1
    
    @staticmethod
    def showCounter():
        return Car.__counter

# Creating objects
maruti = Car()
bmw = Car()
print(Car.showCounter())

honda = Car()
print(Car.showCounter()) # We cannot run static method using objects

# `Q-2:` Create a deck of cards class. Internally, the deck of cards should use another class, a card class Your requirements are:
"""
* The `Deck` class should have a deal method to deal a single card from the deck
* After a card is dealt, it is removed from the deck.
* There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
* The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

`Deck` Class
* It is class of all possible cards in a deck. Total 52 cards.
* Methods - `deal()` it will take out one card from the deck of cards.
* Deck of cards should get shuffeled while creating the deck object.
* `no of cards remaining in deck - <number>` should dsiplay on printing any deck object.

`Card` class
* It is a class of card
* Atrributes - `suit` and `value`
* `<suit> of <value>` should dsiplay on printing any card object.
"""
import random
class Card:

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self): # The __repr__ method in Python is a special method used to define a string representation of an object.
        return "{}->{}".format(self.suit,self.value) 

class Deck:

    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
        self.cards = [Card(suit,value) for suit in suits for value in values] # Using nested loop inside a list comprehensions
    
    def __str__(self): # If you print the object directly this method will get triggered
        return "Cards left " + str(len(self.cards))

    def shuffle(self):
        if len(self.cards) < 52:
            print('only full deck can be shuffled')
        else:
            random.shuffle(self.cards)
        return self.cards
    
    def delt(self):
        if len(self.cards) == 0:
            print('All cards have been dealt')
        return self.cards.pop()

d = Deck()
d.shuffle() # Shuffling
d.delt() # Pick up the card and remove it from deck
d.shuffle()
d.delt()
print(d)

# Difference between __repr__ and __str__ method -> __repr__is a representation of object without print statment and __str__ is a representation of object when you print the object directly

# `Q-3`: Find the area of a rectangle.
"""
Approach:
- The class name should be _Rectangle_.
- The constructor should accept two parameters *length* and *height* but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
- Create a method called *area()* which has no parameters.
- Create a method called *is_square()* which also has no parameters. Return True if the rectangle is a square otherwise return False.
- If you are using a if-else block inside the *is_square()* method, then use the one-linear syntax.
"""
class Rectangle:
    def __init__(self, length: float, height: float):
        self.length = length
        self.height = height

    @classmethod
    def property(cls, length, bredth):
        return cls(length, bredth) # Returning an object

    def area(self):
        # Return True if the rectangle is a square otherwise return False
        return self.length * self.height

    def is_square(self):
        return True if self.length == self.height else False

obj = Rectangle.property(10, 20)
print(obj.area())
print(obj.is_square())

# `Q-4`: Problem 4
"""
**Statement:** Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.
"""
from datetime import datetime
class Manifacturing:
    def __init__(self, manufacturing_date, expiry_date):
        date_format = "%Y-%m-%d"
        self.manufacturing_date = datetime.strptime(manufacturing_date, date_format)
        self.expiry_date = datetime.strptime(expiry_date, date_format)
    
    def time_require_to_expire(self):
        time_left = self.expiry_date - self.manufacturing_date

        if time_left < 0:
            print("Prodict already expired")
            return None
        else:
            years = time_left.days // 365
            months = (time_left.days % 365) // 30
            days = (time_left.days % 365) % 30
            return years, months, days

manufacturing_date_str = "2023-01-01"
expiry_date_str = "2025-01-01"

product = Manifacturing(manufacturing_date_str, expiry_date_str)
time_left = product.time_require_to_expire()

print("Time left for expiry:", time_left)

# `Q-5:` Problem 5
"""
**Statement:** A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
- Age is greater than 20
- Marks is between 0 and 100 (both inclusive)

A student qualifies for admission, if
- Age and marks are valid and
- Marks is 65 or more

Write a python program to represent the students seeking admission in the university. The details of student class are given below.
"""
class Admission:
    def __init__(self):
        self.__id = None
        self.__age = None
        self.__marks = None
    
    def get_date(self):
        return self.__id, self.__age, self.__marks
    
    def set_date(self, roll_id: int, age: int, marks: int):
        self.__id = roll_id
        self.__age = age
        self.__marks = marks
    
    def validity(self):
        if self.__age > 20 and self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False
    
    def Qualification(self):
        if self.validity() and self.__marks > 65:
            print("You are eligible for adimission")
        else:
            print("You are not eligible for adimission")

rohit = Admission()
rohit.set_date(124, 23, 68)
rohit.get_date()
rohit.Qualification()

# `Q-6:` Ice-Cream Scoops and Bowl shop
"""
1. Create a class `Scoop` which has one public property `flavor` and one private proptery `price`. Take `flavor` values during object creation.
2. Create a class `Bowl` with private prperty `scoop_list` which will have list of scoopd object.
3. Create a method `add_scoops` in `Bowl` class which will add any no of `Scoop` objects given as parameter and store it in `scoops_list`.
4. Make getter and setter method for `price` property.
5. Make a method `display` to display `flavour` and `price` of each `Scoop` in `scoop_list` and print total price of the bowl by adding all flavour scoops prices.

6. Make a method `sold` in both `Scoop` class and `Bowl` class to print no of quantity sold.

Ex.-
```
choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

print(bowl)

bowl.display()

Scoop.sold()
Bowl.sold()

```

`Output`
```
Flavor - chocolate Price - None
Flavor - berry Price - 120
chocolate
berry
vanilla
Dsiplaying Bowl
Flavor - chocolate Price - 100
Flavor - berry Price - 120
Flavor - vanilla Price - 150
Price of Bowl - 370
3 scoops sold
1 bowls sold

```
"""
class Scoop:
    __total_scoops = 0

    def __init__(self, flavor):
        self.flavor = flavor
        self.__price = None
        Scoop.__total_scoops += 1
    
    # Getter
    def get_price(self):
        return self.__price
    # Setter
    def set_price(self, new_price):
        self.__price = new_price
    
    def __str__(self):
        return f"Flavor - {self.flavor} Price - {self.get_price()}"
    
    def __repr__(self):
        return self.flavor
    
    @staticmethod
    def sold():
        print(Scoop.__total_scoops)
    
class Bowl:
    __total_bowls = 0
    def __init__(self):
        self.scoop_list = []
        Bowl.__total_bowls += 1
    
    def add_scoops(self, *scoop_obj):
        for obj in scoop_obj:
            self.scoop_list.append(obj)
    
    def display(self):
        total_price = 0
        for obj in self.scoop_list:
            print(obj.flavor, "-", obj.get_price())
            total_price += obj.get_price()
        print("The total price - ", total_price)
    
    def show(self):
        return self.scoop_list

    def __str__(self):
        return "\n".join([obj.flavor for obj in self.scoop_list])
    
    @staticmethod
    def sold():
        print(Bowl.__total_bowls)

choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scenerios

print(bowl.show())

print(bowl)

bowl.display()

Scoop.sold()
Bowl.sold()