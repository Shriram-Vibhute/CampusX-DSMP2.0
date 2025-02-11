# Q1: Print the given strings in the specified format.
print("Data", "Science", "Mentorship", "Program", "started", "By", "CampusX", sep='-')

# Q2: Convert Celsius value to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Q3: Swap two numbers without using any special Python syntax.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print(f"a = {a}, b = {b}")

# Q4: Find the Euclidean distance between two coordinates.
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))
distance = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
print(f"Distance: {distance}")

# Q5: Calculate simple interest.
principle = float(input("Enter principle amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time_period = float(input("Enter time period in years: "))
simple_interest = (principle * rate_of_interest * time_period) / 100
print(f"Simple Interest: {simple_interest}")

# Q6: Determine the number of dogs and chickens given the total number of heads and legs.
heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))
chickens = (4 * heads - legs) / 2
dogs = heads - chickens
print(f"Chickens: {int(chickens)}")
print(f"Dogs: {int(dogs)}")

# Q7: Find the sum of squares of the first n natural numbers.
n = int(input("Enter the number: "))
sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
print(f"Sum of squares: {sum_of_squares}")

# Q8: Find the Nth term of an Arithmetic Series.
first_term = int(input("Enter the first term: "))
second_term = int(input("Enter the second term: "))
nth_term = int(input("Enter the value of n: "))
common_difference = second_term - first_term
n_term = first_term + (nth_term - 1) * common_difference
print(f"Nth term: {n_term}")

# Q9: Find the sum of two fractions.
num1 = int(input("Enter numerator of the first fraction: "))
den1 = int(input("Enter denominator of the first fraction: "))
num2 = int(input("Enter numerator of the second fraction: "))
den2 = int(input("Enter denominator of the second fraction: "))
fraction_sum = ((num1 * den2) + (num2 * den1)) / (den1 * den2)
print(f"Sum of fractions: {fraction_sum}")

# Q10: Calculate the number of glasses of milk that can be obtained from a milk tank.
length = int(input("Enter the length of the milk tank: "))
breadth = int(input("Enter the breadth of the milk tank: "))
height = int(input("Enter the height of the milk tank: "))
glass_height = int(input("Enter the height of the glass: "))
glass_radius = int(input("Enter the radius of the glass: "))
tank_volume = length * breadth * height
glass_volume = 3.14 * glass_radius**2 * glass_height
number_of_glasses = int(tank_volume / glass_volume)
print(f"Number of glasses: {number_of_glasses}")
