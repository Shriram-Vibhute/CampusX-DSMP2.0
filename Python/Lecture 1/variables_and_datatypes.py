# Everything in Python is created by an object
a = 10  # an integer object
a = 5.875685  # reassigns 'a' to a float object
print(type(a))  # prints the type of 'a', which is now <class 'float'>

b = None  # 'None' is a special object representing the absence of value, of type 'NoneType'
print("The type of b is : ", type(b))  # prints the type of 'b', which is <class 'NoneType'>

print(type('python')) # prints the type of the string literal, which is <class 'str'>

c = [1, "dexter", {"age": 21}, 4.6]  # a list object containing different types of elements, lists are mutable
d = (1, "dexter", {"age": 21}, 4.6)  # a tuple object containing different types of elements, tuples are immutable

e = {
    "name": "Dexter",
    "college": "ABCD",
    'age': 69,
    True: "Whether redundant keys are possible to store in this",
    True: "Keys are in any form",
    None: 10
}  # a dictionary object with mixed keys, the second True key will overwrite the first one
print(type(e))  # prints the type of 'e', which is <class 'dict'>
print(e[None])
print(e[True])  # prints the value associated with the True key, which will be "Keys are in any form"

f = {'Hello', 'World', 'Welcome'}  # a unordered set object containing unique elements, order is not guaranteed
print(f)  # prints the set 'f', order of elements may vary