# def dfs(s):
#     cnt = 1
#     visited[s] = True

#     for n in v[s]:
#         if visited[n]:
#             continue
#         cnt += dfs(n)
#     return cnt

# V = int(input())
# E = int(input())
# v = [[] for i in range(V + 1)]
# visited = [False for i in range(V + 1)]

# for _ in range(E):
#     a, b = map(int, input().split())

#     v[a].append(b)
#     v[b].append(a)
# print(dfs(1)-1)
# #########3333

# def dfs(s):
#     cnt = 1
#     visited[s] = True

#     for n in g[s]:
#         if visited[n] == 1:
#             continue
                
#         cnt += dfs(n)
#     return cnt



# V = int(input())
# E = int(input())
# g = [[] for _ in range(V+1)]
# visited = [[0] for _ in range(V+1)]
# for _ in range(E):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)

# print(dfs(1)-1)
# print(g)
# print(visited)

####




V = int(input())
E = int(input())
g = [[] for _ in range(V+1)]
visited = [0] *(V+1)
for _ in range(E):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(s):
    global cnt
    visited[s]=True
    for n in g[s]:
        if not visited[n]:
            cnt += 1
            dfs(n)

cnt = 0

dfs(1)
print(cnt)
print(visited)

