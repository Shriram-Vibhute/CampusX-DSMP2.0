# Taking Single Input
from functools import reduce

a = input("Enter your name: ")  # takes user input and stores it as a string in 'a'
print("My name is", a)  # prints the entered name

x = input("Enter first number: ")  # takes user input for the first number, stored as a string in 'x'
y = input("Enter second number: ")  # takes user input for the second number, stored as a string in 'y'
print(x + y)  # concatenates the strings 'x' and 'y', prints the result

print(int(x) + int(y))  # converts 'x' and 'y' to integers and prints their sum

z = bool(input('Are you more than 18 years old? '))  # takes user input and converts it to a boolean (not directly useful as 'input' returns string)

# Taking Multiple Inputs
# Method 1: Using split method
a, b, *c = input("Enter the value in one line separated by space : ").split(' ')  # splits the input string by spaces and assigns to 'a', 'b', 'c'
print(int(a) + int(b) + (reduce(lambda x, y: int(x) + int(y), c) if type(c) == list else int(c)))  # converts 'a', 'b', and 'c' to integers and prints their sum
# This will work because if you want to define a tupule with only one element, you need to add a comma after the element but if you don't add a comma, it will be considered as an int just like above eg.

# Method 2: List comprehensions
a = list[int](int(input("Enter the value: ")) for i in range(5) if i != 2)  # list comprehension to get 4 integer inputs, skips at i = 2
print(a)
b = [int(input(f'Enter the {i} value: ')) for i in range(5)]  # list comprehension to get 5 integer inputs