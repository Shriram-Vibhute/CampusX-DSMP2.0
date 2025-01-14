# Sequence sum 1/1! + 2/2! + 3/3! + .. 
n = int(input("Enter the number of terms : "))
denominator = 1
ans = 0
for i in range(1, n + 1):
  denominator *= i
  ans += i / denominator
print(ans)

# Nested Loops - Pattern Problems - 1
rows = int(input('enter number of rows : '))
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print('*', end = '')
  print()

# Pattern Problem - 2
rows = int(input('enter number of rows'))
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print(j, end = '')
  for j in range(i - 1, 0, -1):
    print(j, end = '')
  print()

# Loop Control Statement
'''
- Break
- Continue
- Pass
'''
for i in range(1,10):
  if i == 5:
    break
  print(i)

lower = int(input('enter lower range'))
upper = int(input('enter upper range'))
for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j == 0:
      break
  else:
    print(i)

for i in range(1,10):
  if i == 5:
    continue
  print(i)

for i in range(1,10):
  pass # This is actually used if you want to write a block of code but you don't want to write anything in it.