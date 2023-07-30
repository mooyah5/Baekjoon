list_ = []
for _ in range(3):
    list_.append(list(map(int, input().split())))
a = []
b = []
for i in list_:
    a.append(i[0])
    b.append(i[1])

for i in range(3):
    if a.count(a[i]) == 1:
        x = a[i]
    if b.count(b[i]) == 1:
        y = b[i]

print(x, y)