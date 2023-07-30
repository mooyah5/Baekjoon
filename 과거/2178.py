import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(si, sj):
    q = deque()
    v = [[False]*m for _ in range(n)]
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        size = len(q)
        cnt += 1

        for _ in range(size):
            ci, cj = q.popleft()

            if ci == n-1 and cj == m-1:
                return cnt

            for i in range(4):
                ni = ci + dx[i]
                nj = cj + dy[i]

                if ni < 0 or ni > n-1 or nj < 0  or nj > m-1 or arr[ni][nj] == 0 or v[ni][nj] == 1:
                    continue
                
                q.append((ni, nj))
                v[ni][nj] = 1



n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

print(bfs(0,0))



# import sys
# from collections import deque

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(si, sj):
#     cnt = 0
#     q = deque()
#     v = [[False] * m for _ in range(n)]
    
#     q.append((si, sj))
#     v[si][sj] = 1
    
#     while q:
    
#         ci, cj = q.popleft()
#         cnt += 1
#         if ci == n-1 and cj == m-1:
#             return cnt

#         for i in range(4):
#             ni = ci+dx[i]
#             nj = cj+dy[i]
            
#             if not (0 <= ni < n and 0 <= nj < m) or arr[ni][nj] != 1 or v[ni][nj]:
#                 # 인덱스 순서 유의
#                 continue

#             q.append((ni, nj))
#             v[ni][nj]= 1

# n, m = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# # cnt = 0
# # bfs(0, 0)
# print(bfs(0,0))

'''
4 6
101111
101010
101010
111001

'''

# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().rstrip())))
    
    
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# def bfs(x, y):
#     q = deque()
#     v = [[False for i in range(m)] for j in range(n)]
#     cnt = 0
    
#     que.append([x, y])
#     visited[x][y] = True
    
#     while len(que) > 0:
#         size = len(que)
#         cnt += 1
        
#         for _ in range(size):
#             x = que[0][0]
#             y = que[0][1]
#             que.popleft()
            
#             if (x == n - 1) and (y == m - 1):
#                 return cnt
            
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
                
#                 if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 1 or visited[nx][ny]:
#                     continue
                
#                 que.append([nx, ny])
#                 visited[nx][ny] = True               
    
# print(bfs(0, 0))



##

# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().rstrip())))
    
    
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# def bfs(x, y):
#     que = deque()
#     visited = [[False for i in range(m)] for j in range(n)]
#     cnt = 0
    
#     que.append([x, y])
#     visited[x][y] = True
    
#     while len(que) > 0:
#         size = len(que)
#         cnt += 1
        
#         for _ in range(size):
#             x = que[0][0]
#             y = que[0][1]
#             que.popleft()
            
#             if (x == n - 1) and (y == m - 1):
#                 return cnt
            
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
                
#                 if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 1 or visited[nx][ny]:
#                     continue
                
#                 que.append([nx, ny])
#                 visited[nx][ny] = True               
    
# print(bfs(0, 0))