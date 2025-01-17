# `Q1:` Join Tuples if similar initial element
'''
While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

For eg.
```
Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
```
'''
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
hashmap = {}
for i in range(len(test_list)):
    if test_list[i][0] in hashmap:
        hashmap[test_list[i][0]].append(test_list[i][1])
    else:
        hashmap[test_list[i][0]] = [test_list[i][0], test_list[i][1]]
ans = []
for key, value in hashmap.items():
    ans.append(tuple(value))

print(ans)

# `Q2:` Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
"""
For eg.
```
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication :

(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

output-(5, 40, 91, 136, 80)
```
"""
tp = (10,)
ans = [i for i in tp] * len(tp)

# Handling first and last item
if len(tp) > 1:
    ans[0] = tp[0] * tp[1]
    ans[-1] = tp[-1] * tp[-2]

# Handling rest of the elements
for i in range(1, len(tp)-1):
    ans[i] = (tp[i] * tp[i-1]) + (tp[i] * tp[i+1])

print(tuple(ans))

# `Q4`: Count no of tuples, list and set from a list
"""
```
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

```
`Output:`

```
List-2
Set-2
Tuples-1
```
"""
lst = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
dct = {
    'List': 0,
    'Set': 0,
    'Tuple': 0
}
for item in lst:
    if type(item) == list:
        dct['List'] += 1
    elif type(item) == tuple:
        dct['Tuple'] += 1
    elif type(item) == set:
        dct['Set'] += 1
    else:
        continue

print(dct)

# `Q5`: Shortlist Students for a Job role
"""
- Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
- Show every students record in form of tuples if matches all required criteria.
- It is assumed that there will be only one primry skill.
- If no such candidate found, print `No such candidate`

`Input:`
```
Enter No of records- 2
Enter Details of student-1
Enter Student name- Manohar
Enter Higher Education- B.Tech
Enter Primary Skill- Python
Enter Year of Graduation- 2022
Enter Details of student-2
Enter Student name- Ponian
Enter Higher Education- B.Sc.
Enter Primary Skill- C++
Enter Year of Graduation- 2020

Enter Job Role Requirement
Enter Skill- Python
Enter Higher Education- B.Tech
Enter Year of Graduation- 2022
```

`Output`
```
('Manohar', 'B.tech', 'Python', '2022')
```
"""
# write your code here
students = []

num = int(input('enter the number of applicants'))

for i in range(num):
  print('Enter details of',i+1,'applicant:')
  name = input('enter name')
  h_ed = input('enter higher education')
  p_skill = input('enter primary skill')
  yog = input('enter year of graduation')

  students.append((name,h_ed,p_skill,yog))

required_skill = input('enter required skill')
required_hed = input('enter required higher education')
required_yog = input('enter required year of graduation')

flag = False
for i in students:
  if i[1] == required_hed and i[2] == required_skill and i[3] == required_yog:
    print(i)
    flag = True

if flag == False:
  print('No such candidates')

# `Q1:` Write a program to find set of common elements in three lists using sets.
"""
```
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]
```
"""
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(list(set(ar1) & set(ar2) & set(ar3)))

# `Q2:` Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
"""
`Input:`
```
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
```
`Output:`
```
No of unique vowels-6
```
"""
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ans, total = set(), 0

for c in Str1:
    if c in vowels:
        if c not in ans:
            ans.add(c)
            total += 1

print("No of unique vowels: ", total)

# `Q4`: find union of n arrays.
'''
**Example 1:**

Input:
```bash
[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
```

Output:

```bash
[1, 2, 3, 4, 5, 6, 7, 9]
```
'''
ans = set()
lst = [[1, 2, 2, 4, 3, 6],[5, 1, 3, 4],[9, 5, 7, 1],[2, 4, 1, 3]]
for i in lst:
    ans.update(i)

print(ans)

# `Q1`: Key with maximum unique values
"""
Given a dictionary with values list, extract key whose value has most unique values.

**Example 1:**

Input:

```bash
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
CampusX
```

**Example 2:**

Input:
```bash
test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
Best
```
"""
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
max_unique_elements, max_unique_elements_key = 0, None
for key, value in test_dict.items():
    if len(set(value)) > max_unique_elements:
        max_unique_elements_key = key
        max_unique_elements = len(set(value))

print(max_unique_elements_key)

# `Q2`: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.
"""
**Example 1:**

Input:

```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
```

Output:

```bash
CampusX is the best channel for Data-Science students.
```

**Example 2:**

Input:
```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
```

Output:
```bash
CampusX best for DS students.
```
"""
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

test_str = test_str.split()
for i in range(len(test_str)):
    if test_str[i] in repl_dict:
        test_str[i] = repl_dict[test_str[i]]

test_str = " ".join(test_str)
print(test_str)

# `Q4`: Convert a list of Tuples into Dictionary.
"""
**Example 1:**

Input:
```bash
[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
```

Output:
```bash
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
```

**Example 2:**

Input:
```bash
[('A', 1), ('B', 2), ('C', 3)]
```

Output:
```bash
{'A': [1], 'B': [2], 'C': [3]}
```
"""
q = [('A', 1), ('B', 2), ('C', 3)]
dt = {}
for i in q:
    dt[i[0]] = [i[1]]
print(dt)

# `Q5`: Sort Dictionary key and values List.
"""
**Example 1:**

Input:

```bash
{'c': [3], 'b': [12, 10], 'a': [19, 4]}
```

Output:

```bash
{'a': [4, 19], 'b': [10, 12], 'c': [3]}
```

**Example 2:**

Input:

```bash
{'c': [10, 34, 3]}
```

Output:

```bash
{'c': [3, 10, 34]}
```
"""
dt = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

# Sorting keys
dt_keys = sorted(dt.keys())
new_dt = {key: dt[key] for key in dt_keys}

# sorting values
for key, value in new_dt.items():
    # Sorting Values
    new_dt[key].sort()

print(new_dt)