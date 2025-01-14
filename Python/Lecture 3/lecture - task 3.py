# `Problem 1` - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
n = int(input("Enter the number : "))
for i in range(1, n+1):
  for j in range(n - i + 1, 0, -1):
    print(j, end = ' ')
  print()

# `Problem 2`: Print the following pattern.
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n = int(input("Enter the number : "))
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print('*', end = ' ')
  print()
for i in range(1, n):
  for j in range(n - i, 0, -1):
    print('*', end = ' ')
  print()

# `Problem 3`:Write a program to print the following pattern
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n = int(input("Enter the number : "))
for i in range(1, n + 1):
  for j in range(1, 2 * n):
    if(j > n - i and j < n + i):
      print("*", end = '')
    else:
      print(' ', end = '')
  print()

# `Problem 5`: Write a Python Program to Find the Sum of the Series till the nth term: 1 + x^2/2 + x^3/3 + … x^n/n, n will be provided by the user
n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
total_sum = 1
for i in range(2, n + 1):
  total_sum += (i ** i / i)
print(total_sum)

# `Problem 7` - Find the sum of the series upto n terms.
'''
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.
'''
n = int(input("Enter the value of n: "))
total_sum, addition_factor = 0, 0
for i in range(0, n):
  addition_factor = addition_factor * 10 + 2
  total_sum += addition_factor
print(total_sum)

"""###`Problem 8`: Write a program to print all the unique combinations of 1,2,3 and 4

`Output`:
```
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
.
.
and so on
```
"""

# Code here

"""###`Problem 9`: Write a program that will take a decimal number as input and prints out the binary equivalent of the number"""
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number < 0:
        return "-" + decimal_to_binary(-decimal_number)
    
    binary = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number //= 2
    
    return binary

# Input from the user
decimal_number = int(input("Enter a decimal number: "))
binary_equivalent = decimal_to_binary(decimal_number)

print(f"The binary equivalent of {decimal_number} is {binary_equivalent}")

# `Problem 10`: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers - It have the optimized solution as well
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2st number : "))

small_number = a if a <= b else b
for i in range(small_number, 0, -1):
  if int(a % i) == 0 and int(b % i) == 0:
    HCF = i
    print('HCF -> ', HCF)
    break

print('LCM ->', a * b / HCF)

"""### **Problem 11:** Create Short Form from initial character
Given a string create short form ofthe string from Initial character. Short form should be capitalised.

Example:

`Input:`
```
Data science mentorship program
```

`Output:`
```
DSMP
```
"""
string = input("Your string : ")
lst = string.split()
print(''.join([i[0].upper() for i in lst]))

"""###`Problem 12`: Append second string in the middle of first string

`Input:`
```
campusx
data
```
`Output`:

```
camdatapusx
```
"""
string = input("Your string : ")
additional_string = input("additional string : ")
updated_str = string[:int(len(string) / 2)] + additional_string
updated_str += string[int(len(string) / 2):]
print(updated_str)

# `Problem 13`:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Lets apply two-pointer approach
string = input("Enter your string : ") # We have to split this because strings itself are immutable
string = [cr for cr in string]
left, right = 0, len(string) - 1
i = 0
while left != right:
  if string[i].islower():
    string[i], string[left] = string[left], string[i]
    left += 1
    i += 1
  else:
    string[i], string[right] = string[right], string[i]
    right -= 1

print("".join(string))


"""### `Problem 14:`Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.

Input:

`hel123O4every093`

Output:

```
Sum: 22
Avg: 3.142
```
"""
string = input("Enter your string : ")
total_sum, total_digits = 0, 0
for i in string:
  if i.isnumeric():
    total_sum += int(i)
    total_digits += 1

print("Total sum : ", total_sum)
print("Average : ", total_sum / total_digits)

"""### `Problem 16`: Check whether the string is Symmetrical.

**Statement:** Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

**Example 1:**

`Input`

```bash
khokho
```

`Output`

```bash
The entered string is symmetrical
```
"""

string = input("Enter your string : ")
def isSymmetric(string: str) -> bool:
  if (len(string) % 2 != 0): return False
  else:
    for i in range(len(string) // 2):
      if (string[i] != string[len(string) // 2 + i]):
        return False
  return True

print("Symmetric" if isSymmetric(string) else "Not Symmetric")

# `Problem 20`: Write a program that can remove all the duplicate characters from a string. User will provide the input

string = input("Enter the string : ")
string = [c for c in string]
ans = ""
for c in string:
  if c not in ans:
    ans += c

print(ans)