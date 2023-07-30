N, M = map(int, input().split())
mat = [input() for _ in range(N)]

for i in range(1, N-1):
    for j in range(1, M-1):
        if mat[i][j] == 'R':
            ry = i
            rx = j
        elif mat[i][j] == 'B':
            by = i
            bx = j

di = [1, 0, -1, 0] # 우 하 좌 상
dj = [0, 1, 0, -1]

for i in range(1, N-1):
    for j in range(1, M-1):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                