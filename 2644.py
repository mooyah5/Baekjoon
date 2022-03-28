from collections import deque

n = int(input())    # 전체 사람 수
p1, p2 = map(int, input().split()) # 촌수 계산할 사람 번호
m = int(input())
G = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input())
    G[a].append(b)
    G[b].append(a)

def bfs(v, cnt):
    visited = [False for i in range(n+1)]
    visited[v] = True

    for nxt in G[v]:
        if visited[nxt]:
            continue
        bfs(v, cnt+1)

bfs(p1, 0)