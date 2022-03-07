def yak(arr):
    a = arr[-1] * arr[0]
    x = []
    for l in arr:
        if a % l == 0:
            return a
        else:
            x.append(l)
    for i in x:
        a *= i
    return a

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(yak(arr))
