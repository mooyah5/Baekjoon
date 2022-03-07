import sys
T = int(input())
a = list(map(int, input().split()))
a.sort()

s = a[0]
e = a[-1]

for i in a:
    