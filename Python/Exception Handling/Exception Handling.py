# This script demonstrates various exception handling techniques in Python, including try-except-finally,
# try-except-else, nested try-except, exception handling in functions, and raising custom errors.

# Try Except Finally
a = int(input('Enter your number : '))  # Prompt user for input and convert to integer
try:
    print(a / 0)  # Attempt to divide by zero, which will raise a ZeroDivisionError

except ValueError as ve:
    print('Value Error Message: ', ve)  # Handle ValueError if input is not an integer

except SyntaxError as se:
    print('Syntax Error Message: ', se)  # Handle SyntaxError (not likely to occur here)

except ZeroDivisionError as ze:
    print('Zero Division Error Message: ', ze)  # Handle division by zero error

except Exception as e:
    print('error message: ', e)  # Handle any other exceptions

finally:
    print("The Error is not Resolved")  # This block will always execute, regardless of errors


# Try Except Else
a = input('Enter a number : ')  # Prompt user for input
try:
    string = int(a)  # Attempt to convert input to integer
except ValueError as ve:
    print('Error - ', ve)  # Handle ValueError if input is not an integer
except Exception as e:
    print(e)  # Handle any other exceptions
else:
    print('There is no error found')  # This block runs only if no exceptions were raised


# Nested Try-Except
a = input("Enter The Value -> ")  # Prompt user for input
try:
    global b  # Declare b as a global variable
    b = int(a)  # Attempt to convert input to integer
except:
    print('Warning -> Dont send values other than integers')  # Warn if conversion fails
    a = input("Enter the Value -> ")  # Prompt for input again
    try:
        b = int(a)  # Attempt to convert input to integer again
    except Exception as e:
        print("Error -> ", e)  # Handle any exceptions that occur
    else:
        print('Your age will be set')  # Confirm successful conversion
    finally:
        print('Lets Wait')  # This block will always execute
else:
    print('Log in successful')  # This block runs only if no exceptions were raised
finally:
    print('Done')  # This block will always execute


# Exception Handling in Function
def exceptin_handling(val: int):
    try:
        print(val / 0)  # Attempt to divide by zero
    except Exception as e:
        print(e)  # Handle any exceptions that occur
    finally:
        print('Done')  # This block will always execute

exceptin_handling(10)  # Call the function with an integer


# Raising Custom Errors
a = int(input('Enter your GE -> '))  # Prompt user for input
if a < 18:
    try:
        raise Exception("Age not valid")  # Raise a custom exception if age is less than 18
    except Exception as e:
        print("The error message is - ", e)  # Handle the custom exception
else:
    print('ok')  # Confirm valid age

x = "hello"  # Example variable

if not type(x) is int:  # Check if x is not an integer
    raise TypeError("Only integers are allowed")  # Raise a TypeError if x is not an integer

# if else in try-except
try:
    a = int(input("Enter your age : "))
    if a < 18:
        raise ValueError("Your age is too less for this role")
    else:
        print("Your are elegiable for this role")
except ValueError as v:
    print("Your error is - ", v)

# Exceptions under loop
for i in range(5):
    try:
        raise ValueError("You are underage") if i < 4 else print("you are ok")
    except Exception as e:
        print("Error Message - ", e)

# Loops under Exceptions
try:
    for i in range(5):
        if(i == 4):
            raise ValueError("Error")
        else:
            print(i)
except Exception as e:
    print("Error occured")