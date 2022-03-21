from collections import deque

def Del():
    global q
    q = deque()
    if len(q) <= 2:
        print(q.pop())
        return
    else:
        q.popleft()
        tmp = q.popleft()
        q.append(tmp)
        Del()

N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)
Del()