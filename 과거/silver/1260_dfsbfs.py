from collections import deque

def DFS(v):
    global visited_d
    q = []
    q.append(v)
    visited_d[v] = 1

    while q:
        c = q.pop(0)
        i = 0
        while i < V:
            if graph[c][i] == 1 and visited_d[c] == 0:
                res.append(i)

            i += 1





def BFS(v):
    q = deque()
    q.append(v)

    pass



V, E, v = map(int, input().split()) # 정점개수, 노드개수, 시작점
arr = []
graph = [[0] * (V+1) for _ in range(V+1)]
visited_d = [0] * (V+1)
res = []

for _ in range(E):  # 간선의 개수만큼
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

DFS(v)
print(res)
BFS(1)