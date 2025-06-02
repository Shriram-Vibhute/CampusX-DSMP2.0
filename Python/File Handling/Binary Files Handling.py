# Problems with working in text mode
'''
- can't work with binary files like images
- not good for other data types like int/float/list/tuples
'''

# working with binary file
with open('screenshot1.png','r') as f:
  f.read() # Throws an error

# working with binary file
with open('screenshot1.png','rb') as f:
  with open('screenshot_copy.png','wb') as wf: # THis file will create is not already present in current directory
    wf.write(f.read()) # reading one file and writing onto another

# working with a big binary file

# working with other data types
with open('sample.txt','w') as f:
  f.write(5) # Throws an error - you can only write string in the files not any other datatypes

with open('sample.txt','w') as f:
  f.write('5')

with open('sample.txt','r') as f:
  print(int(f.read()) + 5)

# more complex data
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}

with open('sample1.txt','w') as f:
  f.write(str(d))

with open('sample.txt','r') as f:
  print(dict(f.read())) # Throws an error - string cannot able to convert into dictonary

# Serialization and Deserialization
'''
- Serialization - process of converting python data types to JSON format
- Deserialization - process of converting JSON to python data types
'''

# What is JSON? - A universally accepted datatype which is present in all the programming languages

# serialization using json module
# list
import json

L = [1,2,3,4]

with open('demo.json','w') as f:
  json.dump(L,f)

# dict
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}

with open('demo.json','w') as f:
  json.dump(d, f, indent=4) # Serialization


# deserialization
import json

with open('demo.json', 'r') as f:
  j = json.load(f)
  print(j['name'])

with open('demo.json','r') as f:
  d = json.load(f) # d is an object by which you can access all the keys
  print(d)
  print(type(d))

# serialize and deserialize tuple
import json

t = (1,2,3,4,5)

with open('demo.json','w') as f:
  json.dump(t,f) # When you store tuple in the json file then, it will get stored in the form of list and not in the tuple.
  # When you deserialize it the result is also in the from of list only

# serialize and deserialize a nested dict
import json
d = {
    'student':'nitish',
     'marks':[23,14,34,45,56]
}

with open('demo.json','w') as f:
  json.dump(d,f)

# Serializing and Deserializing custom objects
import json
class Person:

  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

# format to printed in
# -> Nitish Singh age -> 33 gender -> male

person = Person('Nitish','Singh',33,'male')

# As a string
import json

# Note - You have to searilize an object in different way else error - Object of type Person is not JSON serializable
def show_object(person):
  if isinstance(person,Person):
    return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)

import json
# As a dict

def show_object(person):
  if isinstance(person,Person):
    return {'name':person.fname + ' ' + person.lname,'age':person.age,'gender':person.gender}

with open('demo.json','w') as f:
  json.dump(person,f,default=show_object,indent=4)

# indent arrtribute
# As a dict

# deserializing
import json

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d)) # The type is what you stored during writing into the file

# Pickling
'''
`Pickling` is the process whereby a Python object hierarchy is converted into a byte stream, and `unpickling` is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.
'''

class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display_info(self):
    print('Hi my name is',self.name,'and I am ',self.age,'years old')

p = Person('nitish',33)

# pickle dump
import pickle
with open('person.pkl','wb') as f:
  pickle.dump(p,f)

# pickle load
import pickle
with open('person.pkl','rb') as f:
  p = pickle.load(f)

p.display_info()

# Pickle Vs Json
'''
- Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.
'''

# Error - When you run a pickle file on your devide which is made onto another device you will get an error - Cant get attribut 'class_name' on module __main__ - This is because The error you're encountering is likely due to the fact that the class definition of the object being unpickled is not available in the current namespace. When you pickle an object, the pickle module stores the module and class names, but not the actual class definition. When you unpickle the object, Python needs to be able to find the class definition in the same module and with the same name.