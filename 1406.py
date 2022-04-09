# 에디터 S3
from collections import deque
s = deque(map(str,input()))
i = len(s)-1
n = int(input())
for j in range(n):
    com = input().split()
    if len(com) > 1:
        P, Z = com
        if i != 0:
            s.insert(i+1, Z)
        else:
            s.insert(0, Z)
    if com == ['L'] and i != 0:
            i -= 1
    elif com == ['D']:
        if i != len(s)-1:
            i += 1
    elif com == ['B']:
        if i != 0 and s:
            s.pop(i-1) ##
print(s)