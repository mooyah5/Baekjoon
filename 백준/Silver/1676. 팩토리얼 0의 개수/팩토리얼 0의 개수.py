def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n = int(input())

n = str(factorial(n))
for i in range(len(n) - 1, -1, -1):
    if int(n[i]) > 0:
        print(len(n) - i - 1)
        break