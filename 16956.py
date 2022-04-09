# 늑대와 양 S3 bfs

# 크기가 r * c 인 목장, 비어있거나, 양, 늑대가 있다.
# 양은 이동하지 않고, 늑대는 인접칸을 자유롭게 이동
# 목장에 울타리를 설치해 늑대가 양으로 접근 못하게 하려 함

# 첫째 줄 R, C
# 둘째줄부터 목장 . 빈칸, S 양, W 늑대

# 가능하면 첫째줄에 1 출력 후 둘째줄부터 목장상태 (울타리 D)
# 불가능하면 첫째줄에 0 출력 후 종료
from collections import deque
                
r, c = map(int, input().split())
arr = [list(map(str,input())) for i in range(r)]
visited = [[0]*c for i in range(r)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    global visited
    visited[si][sj] = 1
    
    while q:
        ci, cj = q.popleft()
        for i, j in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+i, cj+j
            if not(0<=ni<c and 0<=nj<r) or visited[ni][nj]:
                continue
            if arr[ni][nj] == 'S':
                arr[ci][cj] == 'D'
            visited[ni][nj] == 1
            q.append((ni,nj))

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            bfs(i, j)
print(arr)