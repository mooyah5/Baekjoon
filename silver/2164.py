# 카드2
# S4
# 자료구조, 큐, deque

from collections import deque

N = int(input())

q = deque()
for i in range(1, N + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)

print(q.pop())
