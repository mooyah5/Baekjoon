import sys

T = int(input())
data = []
for i in range(T):
    data.append(input().split())
a = []
for i in range(T):
    data[i][0] = int(data[i][0])
    a.append(data[i][0])
print(a)

b = []
for i in range(T):
    for j in data[i][1]:
        if j == a[i]:
            b.append
print(data)
