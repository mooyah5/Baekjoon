list_ = list(map(int, input().split()))
val = [1, 1, 2, 2, 2, 8]
pm = []
for i in range(6):
    if list[i] != val[i]:
        pm.append(val[i]-list_[i])
    else:
        pm.append(0)
for i in pm:
    print(i, end=' ')
