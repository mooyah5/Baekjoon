'''
기본
def dfs(v):
    visited[v] = True       # 현재 노드 방문처리

    for nxt in G[v]:        # 주변에 갈 수 있는 곳 중에서
        if visited[nxt]:    # 못가면 컨티뉴
            continue
        dfs(nxt)            # 나머지는 들어간다
'''

####




# V = int(input())
# E = int(input())
# g = [[] for _ in range(V+1)]
# visited = [0] *(V+1)
# for _ in range(E):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
#
# def dfs(s):
#     global cnt
#     visited[s]=True
#     for n in g[s]:
#         if not visited[n]:
#             cnt += 1
#             dfs(n)
#
# cnt = 0
#
# dfs(1)
# print(cnt)
# print(visited)

### 다시해보기 0327
#
#
# V = int(input())
# E = int(input())
# G = [[] for _ in range(V+1)]
# for _ in range(E):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)
# visited = [False for i in range(V+1)]
#
# def dfs(v):
#     visited[v] = True       # 현재 노드 방문처리
#
#     for nxt in G[v]:        # 주변에 갈 수 있는 곳 중에서
#         if visited[nxt]:    # 못가면 컨티뉴
#             continue
#         dfs(nxt)            # 나머지는 들어간다
#
# cnt = 0
#
# dfs(1)                      # dfs(1)을 돌리면 1과연결된 모든 방문요소가 True가 되니까
# cnt = 0                     # 방문된 곳 수를 세어주면 됨
# for i in range(1, V+1):
#     if visited[i]:
#         cnt += 1
# print(cnt-1)                # 1번노드 빼야돼서 -1

### 혼자서 다시

# V = int(input())    # 정점의 개수
# E = int(input())    # 간선의 개수
# G = [[] for _ in range(V+1)]
# visited = [False for i in range(V+1)]
# for i in range(E):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)
#
# def dfs(v):
#     visited[v] = True       # 방문처리 해주고
#
#     for nxt in G[v]:
#         if visited[nxt]:
#             continue
#         dfs(nxt)
#
# dfs(1)
# cnt = 0
# for i in range(V+1):
#     if visited[i]:
#         cnt += 1
# print(cnt-1)

## 응용 1
# 방문처리 할 때마다 cnt 세기 (True만들 때마다 세기)

# V = int(input())    # 정점의 개수
# E = int(input())    # 간선의 개수
# G = [[] for _ in range(V+1)]
# visited = [False for i in range(V+1)]
# for i in range(E):
#     a, b = map(int, input().split())
#     G[a].append(b)
#     G[b].append(a)
#
# def dfs(v):
#     global cnt
#
#     visited[v] = True       # 방문처리 해주고
#     cnt += 1
#
#     for nxt in G[v]:
#         if visited[nxt]:
#             continue
#         dfs(nxt)
#
# cnt = 0
# dfs(1)
#
# print(cnt-1)

## 응용 2
#


V = int(input())    # 정점의 개수
E = int(input())    # 간선의 개수
G = [[] for _ in range(V+1)]
visited = [False for i in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(v):
    cnt = 1
    visited[v] = True       # 방문처리 해주고

    for nxt in G[v]:
        if visited[nxt]:
            continue
        cnt += dfs(nxt)
    return cnt

print(dfs(1)-1)