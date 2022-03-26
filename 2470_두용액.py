

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s, e = 0, n-1
x, y = arr[s], arr[e]
while s < e:
    if abs(x+y) > abs(arr[s] + arr[e]):
        x = arr[s]
        y = arr[e]

    if arr[s] + arr[e] < 0:
        s+= 1
    else:
        e -=1

print(x, y)