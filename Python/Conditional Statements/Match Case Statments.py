while True: 
    # Prompt the user to enter their age and convert it to an integer
    a = int(input("Enter Your Age : "))

    # Match the age 'a' with different cases
    match a:
        case 0:
            # If age is 0, exit the loop
            break
        
        case 18:
            # If age is 18, print a specific message about driving speed
            print("You are just starting to drive, Your speed must be under 60kmph")

        # case _: -> This is the default case, but not used here
  
        case _ if a < 17:
            # If age is less than 17, print a message indicating the user cannot drive
            print("You are underage, You cannot drive")

        case _ if a > 18 and a < 60:
            # If age is between 19 and 59 (inclusive), print a message indicating they can drive
            print("You can drive")
        
        case _ if a >= 60:
            # If age is 60 or more, print a message advising caution while driving
            print("Take precautions while driving")



a = 'abc'
match a:
    case 'a':
        print('a')
    case 'b':
        print('b')
    case _ if a is 'abc':
        # The is operator is used to compare the identities of two objects, not their values. This is typically used for comparing objects to their singleton instances, such as None, True, and False. Using is for string comparisons can lead to unexpected behavior because strings are immutable, and while Python may sometimes optimize memory usage by reusing objects for small strings, this is not guaranteed for all cases.
        print('Identity')
    case _ if a == 'abc':
        print('Equality')