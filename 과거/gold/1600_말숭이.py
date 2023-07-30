# 원숭이 나이트처럼 움직이는 건 k번 가능
# 이후로는 상하좌우한칸만가능
from collections import deque

def dfs():
    global cnt
    kcnt = k
    q = deque
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == ax and y == ay:
            return x, y
        if kcnt >= 0:
            for i in range(8):
                nx = x + kmove_x[i]
                ny = y + kmove_y[i]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and not mat[nx][ny] == 1 :
                    visited[nx][ny] = 1
                    q.append(nx,ny)
                    kcnt -= 1
                else:
                    nx = x - kmove_x[i]
                    ny = y - kmove_y[i]
        if kcnt <= 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and not mat[nx][ny] == 1 :
                    visited[nx][ny] = 1
                    q.append(nx,ny)
    return '-111111'


k = int(input())
w, h = map(int, input().split())
mat = []
for _ in range(h):
    mat.append(list(map(int, input().split())))

visited = [[0]*(w+1) for _ in range(h+1)]
# s = (1, 1)    #시작점
kmove_x = [2, 2, -2, -2, -1, 1, -1, 1]
kmove_y = [1, -1, 1, -1, -2, -2, 2, 2]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
ax = w-1    # 도착점
ay = h-1

dfs()
print(cnt)