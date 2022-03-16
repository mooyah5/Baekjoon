from collections import deque

def DFS(v):
    visit_dfs[v] = 1        # 시작점 방문처리
    print(v, end = ' ')     # 시작점 출력

    for i in range(1, V+1):
        # 1번노드부터 V번까지 1씩 증가
        # 방문하지 않았고,
        # 그래프에 존재하면
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)



def BFS(v):
    q = deque()
    q.append(v)

    pass



V, E, v = map(int, input().split()) # 정점개수, 노드개수, 시작점
arr = []
graph = [[0] * (V+1) for _ in range(n+1)]
visit_dfs = [0] * (V+1)
visit_bfs = [0] * (V+1)

for _ in range(E):  # 간선의 개수만큼
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

DFS(1)
print()
BFS(1)