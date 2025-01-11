# Table of any number
a = int(input("Enter a number : "))

for i in range(a, a * 11, a):
    print(i)
# The third angument is step -> the loop will be in that difference


# iterate over the list
a = ["Dexter", "Shrenik", "Shivraj", "Sushant"]
for names in a:
    # nested for loop
    for chars in names:
        print(chars, end=', ')