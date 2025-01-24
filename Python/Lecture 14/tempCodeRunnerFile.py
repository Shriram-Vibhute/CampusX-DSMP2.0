def decimalToBinary(n, lst):
    if n == 0:
        return None
    decimalToBinary(n // 2, lst)
    lst.append(n % 2)

ans = []
decimalToBinary(9, ans)
print(ans)