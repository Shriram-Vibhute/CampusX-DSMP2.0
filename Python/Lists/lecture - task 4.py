# `Problem 1:` Combine two lists index-wise(columns wise)
'''
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

`Given List:`
```
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
```

`Output:`
```
[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
```
'''

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

ans = []
for item in zip(list1, list2):
    ans.append(list(item))

print(ans)

# `Problem 2:` Add new item to list after a specified item
"""
Write a program to add item 7000 after 6000 in the following Python List
```
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
```
`Output:`
```
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
```
"""

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(2, 7000)
print(list1)

# `Problem 3:` Update no of items available
"""
Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -  
```
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
```

Write a program to show no. of items of each candy type.

`Output:`

```
Jelly Belly-10
Kit Kat-20
Double Bubble-34
Milky Way-74
Three Musketeers-32

```
"""

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

for i in range(len(candy_list)):
    print(f"{candy_list[i]} - {no_of_items[i]}")

# `Problem 4:` Running Sum on list
"""
Write a program to print a list after performing running sum on it.

i.e:

`Input:`
```
list1 = [1,2,3,4,5,6]
```
`Output:`
```
[1,3,6,10,15,21]
```
"""

list1 = [1,2,3,4,5,6]
for i in range(1, len(list1)):
    list1[i] += list1[i - 1]
print(list1)

# `Problem 5:` You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
"""
i.e. Say given list is `[2,4,6,10,1]`
resultant list will be `[22,20,10,23]`.

For 1st element `2` ->> these are greater `(4+6+10)` values and `2` itself so on adding becomes `22`.

For 2nd element `4` ->> greater elements are `(6, 10)` and `4` itself, so on adding `20`

like wise for all other elememts.

`[2,4,6,10,1]`-->`[22,20,16,10,23]`
"""

L = [2,4,6,10,1]

# sort the list
sorted_list = sorted(L)
store_dic = {sorted_list[i]: i for i in range(len(sorted_list))}

# Finding the sum
for i in range(len(sorted_list) - 2, -1, -1):
    sorted_list[i] += sorted_list[i + 1]

# Correcting the sequence
for i in range(len(L)):
    L[i] = sorted_list[store_dic[L[i]]]

print(L)

# `Problem 6:` Find list of common unique items from two list. and show in increasing order
"""
`Input`
```
num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
```

`Output:`
```
[34, 67, 89]
```
"""

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

st = set()
for elem in num1:
    if(elem in num2):
        st.add(elem)
sorted(st)

#`Problem 7:` Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
"""
`Input:`
```
['1ac21', '23fg', '456', '098d','1','kls']
```
`Output:`
```
['456', '23fg', '1ac21', '1', 'kls', '098d']
```
"""

def product(s: str):
    ans = 1
    for elem in s:
        try:
            num = int(elem)
        except Exception as e:
            continue
        else:
            ans *= num
    return ans

lst = ['1ac21', '23fg', '456', '098d','1','kls']
lst.sort(key = product, reverse = True)
lst

# `Problem 8:` Split String of list on K character.
"""
**Example :**

Input:
```bash
['CampusX is a channel', 'for data-science', 'aspirants.']
```

Output:
```bash
['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
```
"""

lst = ['CampusX is a channel', 'for data-science', 'aspirants.']
ans = []
[[ans.append(j) for j in i.split()] for i in lst]
ans

# `Problem 9:` Convert Character Matrix to single String using string comprehension.
"""
**Example 1:**

Input:
```bash
[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
```

Output:
```bash
campux is best channel
```
"""

lst = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
ans = " ".join(["".join(i) for i in lst])
ans

# `Problem 10:` Add Space between Potential Words.
"""
**Example:**

Input:

```bash
['campusxIs', 'bestFor', 'dataScientist']
```

Output:
```bash
['campusx Is', 'best For', 'data Scientist']
```
"""

lst = ['campusxIs', 'bestFor', 'dataScientist']
ans = []
for string in lst:
    temp_str = ""
    for c in string:
        if c.isupper():
            temp_str += (" " + c)
        else:
            temp_str += c
    ans.append(temp_str)
ans

# `Problem 11:` Write a program that can perform union operation on 2 lists
"""
**Example:**

Input:

```bash
[1,2,3,4,5,1]
[2,3,5,7,8]
```

Output:
```bash
[1,2,3,4,5,7,8]
```
"""

a = [1,2,3,4,5,1]
b = [2,3,5,7,8]

ans = []
for i in a:
    if i not in ans:
        ans.append(i)

for i in b:
    if i not in ans:
        ans.append(i)

print(ans)

# `Problem 12:` Write a program that can find the max number of each row of a matrix
"""
**Example:**

Input:

```bash
[[1,2,3],[4,5,6],[7,8,9]]
```

Output:
```bash
[3,6,9]
```
"""

lst = [[1,2,3],[4,5,6],[7,8,9]]
ans = [max(l) for l in lst]
print(ans)

# `Problem 14:` Write a list comprehension that can transpose a given matrix
"""
matrix = [<br>
  [1,2,3],<br>
          [4,5,6],<br>
          [7,8,9]<br>]<br>

[1, 4, 7]<br>
[2, 5, 8]<br>
[3, 6, 9]<br>
"""

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(l)):
    for j in range(i, len(l[i])):
        l[i][j], l[j][i] = l[j][i], l[i][j]

print(l)