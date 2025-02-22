# List Programs

# Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers
L = [1,2,3,4,5,6]
odd, even = [], []
for i in L:
    odd.append(i) if i % 2 == 0 else even.append(i)
print(odd, even)

# How to take list as input from user
l = [input(f"Enter {i}th item : ") for i in range(5)]
print(l)

# Write a program to merge 2 list without using the + operator
L1 = [1,2,3,4]
L2 = [5,6,7,8]
L1.extend(L2)
print(L1)

# Write a program to replace an item with a different item if found in the list
L = [1,2,3,4,5,3]
# replace 3 with 300
L.replace(2, 300)
print(L)

# Write a program that can convert a 2D list to 1D list
L = [[1,2], [3,4], [5,6]]
ans = []
for i in L:
    for j in i:
        ans.append(j)
print(ans)

# Write a program to remove duplicate items from a list
L = [1,2,1,2,3,4,5,3,4]

ans = []
for i in range(len(L)):
    if L[i] not in ans:
        ans.append(L[i])