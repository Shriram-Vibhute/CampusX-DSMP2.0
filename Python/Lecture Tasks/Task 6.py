# Problem 1
"""
Input:

```bash
[1,2,3,3,3,3,4,5]
```

Output:

```bash
[1, 2, 3, 4, 5]
```
"""
# Two pointer approach
def findUnique(arr: list) -> list:
    i, j = 0, 1
    while j < len(arr):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
        j += 1
    return i + 1

arr = sorted([1,2,3,3,3,3,4,5])
print(arr[0:findUnique(arr)])

# `Problem-2:` Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
"""
**Example 1:**

Input:
```bash
green-red-yellow-black-white
```

Output:
```bash
black-green-red-white-yellow
```
"""
def sortString(s: str) -> str:
    # Splitting
    return "-".join(sorted(s.split("-")))

print(sortString("green-red-yellow-black-white"))

# `Problem 5:` Write a Python function to check whether a number is perfect or not.
"""
A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example :

```
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
```
"""
def perfectNumber(n: int) -> bool:
    divisors = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        return True

n = int(input("Enter the number : "))
for i in range(1, n + 1):
    if perfectNumber(i):
        print(i)

"""`Problem-7` Write a python function that accepts a string as input and returns the word with most occurence.

```
Input:
hello how are you i am fine thank you
```

```
Output
you -> 2
```
"""
def countFrequency(s: str) -> str:
    hashMap = {}
    for word in s.split():
        if word not in hashMap:
            hashMap[word] = 1
        else:
            hashMap[word] += 1
    for i in hashMap:
        if hashMap[i] == max(hashMap.values()):
            return i

print(countFrequency("hello how are you i am fine thank you"))

# `Problem-8` Write a python function that receives a list of integers and prints out a histogram of bin size 10
"""
```
Input:
[13,42,15,37,22,39,41,50]
```

```
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}
```
"""
def histogramCreator(arr: list) -> dict:
    ans = {}

    for i in range(len(arr)):
        curr_number = arr[i]
        
        if curr_number % 10 == 0:
            mn = curr_number - 9
            mx = curr_number
        else:
            mn = curr_number - (curr_number % 10) + 1
            mx = curr_number + 10 - (curr_number % 10)
            
        key = f"{mn} - {mx}"

        if key not in ans:
            ans[key] = 1
        else:
            ans[key] += 1
    
    return ans

arr = [13,42,15,37,22,39,41,50]
print(histogramCreator(arr))

# `Problem-10`:Write a python program that receives a list of strings and performs bag of word operation on those strings

lst = [
    "Hello my name is dexter morgan",
    "I am 100 years old",
    "my friend is sleeping",
    "dexter is undercover agent",
    "my school name is 100 states school"
]

# Finding all unique words from list
unique_words = set()
for string in lst:
    for word in string.split():
        unique_words.add(word)

# BOW vector for each string
bow = []
for string in lst:
    words = string.split()
    temp = []
    for word in unique_words:
        if word in words:
            temp.append(1)
        else:
            temp.append(0)
    bow.append(temp)

print(bow)

# `Problem 11:` Write a Python program to add three given lists using Python map and lambda."""
a1 = [1,2,3,4,5]
b1 = [6,7,8,9,10]
c1 = [11,12,13,14,15]

print(list(map(lambda a, b, c: a + b + c, a1, b1, c1)))

# `Problem-13` - Using filter() and list() functions and .lower() method filter all the vowels in a given string.
s = "Hey MY Name IS DexTEr"
s = "".join(list(filter(lambda c: c.lower() not in ['a','e','i','o','u'], s)))
print(s)

# `Problem-14` - Use reduce to convert a 2D list to 1D
import functools
l = [[1,2], [3,4], [5,6]]
print(functools.reduce(lambda a, b: a + b, l))

# Write code here

"""`Problem 15`- A dictionary contains following information about 5 employees:
- First name
- Last name
- Age
- Grade(Skilled,Semi-skilled,Highly skilled)<br>
Write a program using map/filter/reduce to a list of employees(first name + last name) who are highly skilled
"""

# Write code here
employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }

]

list(map(lambda x:x['fname'] + ' ' + x['lname'],list(filter(lambda x:True if x['grade'] == 'highly-skilled' else False,employees))))