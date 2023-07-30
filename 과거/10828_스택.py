import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for i in range(N):
    s = sys.stdin.readline()
    if 'push' in s:
        q.append(int(s[5:]))
    elif 'pop' in s:
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)
    elif 'size' in s:
        print(len(q))
    elif 'empty' in s:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in s:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)