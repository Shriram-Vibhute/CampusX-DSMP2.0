# Problem 1: Calculate in-hand monthly salary after deductions (HRA, DA, PF, and taxes)
salary = int(input("Enter your salary : "))
# HRA, DA, PF deduction
salary -= ((0.1 * salary) + (0.05 * salary) + (0.03 * salary))

if salary >= 500000 and salary < 1000000:
    salary -= (0.1 * salary)
elif salary < 2000000:
    salary -= (0.2 * salary)
else:
    salary -= (0.3 * salary)

print("Your in-hand salary : ", salary)

# Problem 2: Check if three angles can form a triangle
angles = [float(input("Enter angle: ")) for _ in range(3)]
if angles[0] + angles[1] + angles[2] == 180:
    print("Triangle")
else:
    print("Not a triangle")

# Problem 3: Determine profit or loss based on cost price and selling price
cost_price = int(input("Cost Price : "))
selling_price = int(input("Selling Price : "))

print("Profit" if selling_price - cost_price > 0 else "loss")

# Problem 4: Menu-driven program for unit conversions
choice = int(input(
    """
    Enter your choice
    1. cm to ft
    2. km to miles
    3. USD to INR
    4. exit
    """
))

if choice == 1:
    dist = int(input("Enter distance in cm : "))
    print(dist * 0.032)
elif choice == 2:
    dist = int(input("Enter distance in km : "))
    print(dist * 0.62)
elif choice == 3:
    price = int(input("Enter price in usd : "))
    print(price * 91)
else:
    print("exit")

# Problem 5: Display Fibonacci series up to 10 terms using recursion
def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# Problem 6: Find the factorial of a given number using recursion
num = int(input("Enter the number : "))
def factorial(num: int):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(num))

# Problem 7: Reverse a given integer number
num = int(input("Enter your number : "))
print(int(str(num)[::-1]))

# Problem 8: Calculate the sum from 1 to N, skipping multiples of 5 and stopping if the sum exceeds 300
def sum_skip_5(n, current_sum=0):
    if n == 0 or current_sum > 300:
        return current_sum
    if n % 5 == 0:
        return sum_skip_5(n - 1, current_sum)
    return sum_skip_5(n - 1, current_sum + n)

N = int(input("Enter an integer N: "))
result = sum_skip_5(N)
print(result)

# Problem 10: Find numbers between 1000 and 3000 where each digit is even
for i in range(1000, 3001):
    curr_num = i
    status = True
    while curr_num != 0:
        digit = int(curr_num % 10)
        if digit % 2 != 0: 
            status = False
            break
        curr_num //= 10
    if status: 
        print(i)

# Problem 11: Calculate the distance from the origin after a sequence of movements
user_input = [5, 3, 3, 2, 0]
final_x, final_y = 0, 0
for i in range(len(user_input)):
    if i == 0:
        final_y += i
    elif i == 1:
        final_y -= i
    elif i == 2:
        final_x -= i
    else:
        final_x += i

distance = (final_x ** 2 + final_y ** 2) ** 0.5
print(distance)

# Problem 12: Check if a given number is a prime number
num = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Problem 13: Print all Armstrong numbers in a given range
for i in range(int(input("Enter the range : ")) + 1):
    current_num = i
    final_sum = 0
    while current_num != 0:
        final_sum += ((current_num % 10) ** 3)
        current_num //= 10
    if final_sum == i:
        print(i)

# Problem 14: Calculate the angle between the hour hand and minute hand
H = int(input("Enter the hour : "))
M = int(input("Enter the minute : "))
hour_hand_position = 0.5 * M
minute_hand_position = 6 * M
angle = abs(hour_hand_position - minute_hand_position)
print(int(min(360 - angle, angle)))

# Problem 15: Check if two rectangles overlap
LT1 = [int(input("Enter the x coordinate of the left top corner of the first rectangle : ")), int(input("Enter the y coordinate of the left top corner of the first rectangle : "))]
RB1 = [int(input("Enter the x coordinate of the right bottom corner of the first rectangle : ")), int(input("Enter the y coordinate of the right bottom corner of the first rectangle : "))]

LT2 = [int(input("Enter the x coordinate of the left top corner of the second rectangle : ")), int(input("Enter the y coordinate of the left top corner of the second rectangle : "))]
RB2 = [int(input("Enter the x coordinate of the right bottom corner of the second rectangle : ")), int(input("Enter the y coordinate of the right bottom corner of the second rectangle : "))]

if (LT1[0] < RB2[0] or LT2[0] < RB1[0]) and (LT1[1] > RB2[1] or LT2[1] > RB1[1]):
    print("Overlap")
else:
    print("No Overlap")
