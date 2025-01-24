# `Q-1:` Write a function `get_final_line(filename)`, which takes filename as input and return final line of the file.
def get_final_line(filename: str):
    try:
        with open(filename, mode = 'r') as f:
            all_text = f.readlines()
            return all_text[-1]
    except FileNotFoundError as e:
        print("File not found - Creating new file")
        with open(filename, mode = 'w') as f:
            f.write("Some Dummy data")
            all_text = f.readlines()
            return all_text[-1]    
    return None

print(get_final_line('sample.txt'))  


# `Q-2:` Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation -- dictionary."""

def countVowels(filename: str):
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    try:
        with open(filename, mode = 'r') as f:
            data = "Hello"
            while data != "":
                data = f.readline()
        
                # counting the vowels
                for c in data:
                    if c in vowels.keys():
                        vowels[c] += 1
    except FileNotFoundError as e:
        print("Fine not exists")
        return None
    
    return vowels

print(countVowels('sample2.txt'))
                 

#`Q-3:` Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python to read through the file you’ve created. For each line, multiply each first number by the second and include it in the file in third column. In last add a line Total, by summing the value of third column
"""
Input File example: That you need to create
```
1   2
3   4
5   6
7   8
9   10

```

Output File Example:
```
1   2   2
3   4   12
5   6   30
7   8   56
9   10  90
Total   190
```
"""
# Creating a file - and writing init
with open('sample.txt', mode = 'w') as f:
    lst = ['1 2\n', '3 4\n', '298 23\n', '1 -90\n']
    f.writelines(lst)

# Reading the data
ans = []
with open('sample.txt', 'r') as f:
    data = "Hello"
    while data != "":
        data = f.readline()

        # splitting the data
        numbers_as_str = data.split()
        if len(numbers_as_str) == 2:
            num1 = int(numbers_as_str[0])
            num2 = int(numbers_as_str[1])
            product = num1 * num2
            ans_data = f"{num1} {num2} {product}\n"
            ans.append(ans_data)

with open('sample.txt', 'w') as f:
    f.writelines(ans)

        
# `Q-4:` Create line wise reverse of a file
"""
Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).
For example, if a file looks like
 ```
abc def
ghi jkl
```
then the output file will be
```
fed cba
lkj ihg
```
**Notice**: The newline remains at the end of the string, while the rest of the characters are all reversed.
"""
def reverseFile(inputFile: str, outputFile: str):
    with open(inputFile, 'r') as ip:
        with open(outputFile, 'w') as op:
            for data in ip.readlines():
                data = data[::-1]
                op.write(data[1:] + '\n')

reverseFile('sample.txt', 'sample1.txt')


# `Q-5:` Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.
"""
* List of word will be given

Given String

```
strings = '''Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge.'''

word_list = ['alice', 'wonder', 'natural']
```
"""
word_list = ['alice', 'wonder', 'natural']
store = {}
import json
with open('sample.txt', 'r') as f:
    data = f.read().lower()
    for word in word_list:
        store[word] = data.count(word)
json.dump(obj = store, fp = open('sample.json', mode = 'w'))

# Recursion

# **`Q-7:`** Write a function that accepts two numbers and returns their greatest common divisior. Without using any loop
"""
def gcd(int, int) => int

```
gcd(16,24) will give 8
```
"""
def HCF(a, b):
    if b == 0:
        return a
    return HCF(b, a % b)

print(HCF(34, 68))

""" ### `Q-8:` String Edit Distance

 Use your recursive function to write a program that reads two strings from the
user and displays the edit distance between them.

*The edit distance between two strings is a measure of their similarity—the smaller the edit distance, the more similar the strings are with regard to the minimum number of insert, delete and substitute operations needed to transform one string into the other.*

Consider the strings `kitten` and `sitting`. The first string can be transformed
into the second string with the following operations:
* Substitute the `k` with an `s`,
* substitute the `e` with an `i`,
* and insert a `g` at the end of the string.

This is the smallest number of operations that can be performed to transform kitten into sitting. As a result, the edit distance is `3`.


Write a recursive function that computes the edit distance between two strings.

Use the following algorithm:

```
Let s and t be the strings
    If the length of s is 0 then
        Return the length of t
    Else if the length of t is 0 then
        Return the length of s
    Else
        Set cost to 0
        If the last character in s does not equal the last character in t then
            Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all characters except the last one in t, plus 1

        Set d3 equal to the edit distance between all characters except the last one in s, and all characters except the last one in t, plus cost
        Return the minimum of d1, d2 and d3
```
"""

# write code here

"""###`Q-9:` Run-Length Encoding

Run-length encoding is a simple data compression technique that can be effective when repeated values occur at adjacent positions within a list. Compression is achieved by replacing groups of repeated values with one copy of the value, followed by the number of times that the value should be repeated. For example, the list
```
["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
```
would be compressed as `["A", 12, "B", 4, "A", 6, "B", 1]`.

Write a recursive function that implements the run-length compression technique
described above. Your function will take a list or a string as its only parameter. It should return the run-length compressed list as its only result. Include a main program that reads a string from the user, compresses it, and displays the run-length encoded result.
"""

# Write code here

"""###`Q-10:` Write a recursive function to convert a decimal to binary"""
def decimalToBinary(n, lst):
    if n == 0:
        return None
    decimalToBinary(n // 2, lst)
    lst.append(n % 2)

ans = []
decimalToBinary(9, ans)
print(ans)