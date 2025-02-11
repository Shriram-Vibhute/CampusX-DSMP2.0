# multi line strings enclosed in ''' string ''' or """ string """
str = """name : dexter
Age : 45
Country : USA"""

for i in str:
    print(i)

str2 = "Jack Sparrow"
print(str2[10])
# print(str2[12]) # last element of string cannot be accessed -> "\0" like c++

# TypeCasting
a = input("Enter the number : ") # user input is always in string
print(type(a))
a = int(a) # if a is able to convert into int
print(a)

# String Slicing
print("String Slicing")
str = "Jack Sparrow"
print("Length of str : ", len(str))
print(str[0:100])
print(str[:])
print(str[:4])
print(str[2:7])
print(str[2: -1]) # -1 represents -> len(str) - 1; 
print(str[2: len(str)-1])
print(str[-4: -1])
print(str[len(str)-4: len(str)-1])
print(str[len(str)-1: len(str)-4]) # no error but Doen not print enything

# String Methods
str = "Jack Sparrow"
print(str.upper())
str = "!!!Jack Sparro!w!!!!"
print(str.rstrip('!')) # Removes the trailing characters only