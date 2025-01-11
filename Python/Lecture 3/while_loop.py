# while loop with else statement

a = int(input("Enter the number : "))
while a < 10:
    print("Number is less")
    if a == 5:
        break
    a = int(input("Enter the number : "))
else:
    print("Finally You guessed the correct number")

# Else statement will run only when while loop executes completly