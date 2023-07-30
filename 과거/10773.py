import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        q.pop()
    else:
        q.append(n)
if len(q) == 0:
    print(0)
else:
    print(sum(q))
