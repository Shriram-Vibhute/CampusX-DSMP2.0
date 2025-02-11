# Interview Question -> Whether the else block will executed or not
# Ans -> if the for loop successifully get executed till its range then the else will run but if if got break in between then else will not get executed as well

for i in range(6):
    print(i)
    if i == 0:
        break
else:
    print("ok")


# Same goes for while loops as well
i = 10
while i < 4:
    print(++i)
    if i == 4:
        print("Hello")
        break
    i += 1
else:
    print("else got no chills")