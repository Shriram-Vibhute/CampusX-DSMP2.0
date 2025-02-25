import time, operator
def generator():
    start = time.time()
    for i in range(6):
        time.sleep(1)
        print(i + 1)
    end = time.time()
    yield 1, (operator.sub(end, start))

    start = time.time()
    for i in range(6):
        print(i + 1)
    end = time.time()
    yield 2, (operator.sub(end, start))

gen = generator()
print(next(gen))
print(next(gen))
# next(gen) -> this function will run till the end of the last yield statment after it throws an error in between

gen2 = generator()
next(gen2) # You can create another instance to run the code again