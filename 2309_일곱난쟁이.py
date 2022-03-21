arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()

liers_h = sum(arr) - 100

s, e = 0, 8
liers_i = []
while s < e:
    if arr[s] + arr[e] == liers_h:
        arr.remove(arr[e])
        arr.remove(arr[s])
        break
    elif arr[s] + arr[e] < liers_h:
        s += 1
    else:
        e -= 1

for i in arr:
    print(i)
