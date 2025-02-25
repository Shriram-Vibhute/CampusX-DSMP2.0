class class_1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        print(self.a + other.a, self.b + other.b, self.c + other.c)
    
    def __sub__(self, other):
        print(self.a - other.a, self.b - other.b, self.c - other.c)
    
    def __mul__(self, other):
        print(self.a * other.a, self.b * other.b, self.c * other.c)
    
    def __truediv__(self, other):
        print(self.a / other.a, self.b / other.b, self.c / other.c)

c1 = class_1(1,2,3)
c2 = class_1(4,5,6)

c1 + c2
c1 - c2
c1 * c2
c1 / c2

# https://www.geeksforgeeks.org/operator-overloading-in-python/