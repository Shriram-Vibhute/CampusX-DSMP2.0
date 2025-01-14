# Creating a file
f = open('main.txt', 'x')  # Open a new file for exclusive creation
f.close()  # Close the file

# Reading a file
with open('main.txt', mode = 'r') as f:
  print(f.readlines())

f = open('main.txt', 'r')  # Open the file for reading
print(f.readlines())  # Provide a list of all lines in the file
f.close()  # Close the file

f = open('main.txt', 'r')  # Open the file for reading
print(f.read())  # Reads all the content from the file
f.close()  # Close the file

f = open('main.txt', 'r')  # Open the file for reading
for i in range(3):  # Loop to read the first three lines
    print(f.readline())  # Reads content line by line
f.close()  # Close the file

# Writing & Appending a file
f = open('main.txt', 'w')  # Open the file for writing (overwrites existing content)
f.write('Existing content will get vanished and new conttent will get added')  # Write new content
f.close()  # Close the file

f = open('main.txt', 'a')  # Open the file for appending
f.write('New content will get appended')  # Append new content
f.close()  # Close the file

# Deleting the file
import os  # Import the os module
if os.path.exists("demofile.txt"):  # Check if the file exists
  os.remove("demofile.txt")  # Remove the file if it exists
else:
  print("The file does not exist")  # Print message if the file does not exist

# r+ -> read - write mode simultaneously
f = open('main.txt', 'r+')  # Open the file for reading and writing
f.truncate(10)  # Truncate the file to the first 10 bytes
print(f.read())  # Read the content from the file
f.close()  # Close the file

f = open("main.txt", 'w')  # Open the file for writing (overwrites existing content)
f.writelines(['abc\n', 'def\n', 'ghi'])  # Write multiple lines to the file
f.close()  # Close the file

# seek and tell
f = open('main.txt', 'r')  # Open the file for reading
f.seek(5)  # Move the cursor to the 5th byte
print(f.readline())  # Read and print the line from the current cursor position
print(f.tell())  # Print the current cursor position
f.close()  # Close the file