a, b = map(int, input().split())
arr = []
for i in range(1, 46):
    for j in range(i):
        arr.append(i)
sum = 0
for i in range(a-1, b):
    sum += arr[i]
print(sum)