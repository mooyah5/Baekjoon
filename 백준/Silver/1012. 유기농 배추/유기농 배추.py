### 230804 1012 유기농배추
import sys
sys.setrecursionlimit(2500)  # 파이썬 기본 재귀 깊이 제한이 1000으로 얕기 때문에 런타임 에러 발생 방지

def DFS(y, x):
    # global visited
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    visited[y][x] = 1  # 현재 장소 방문
    for k in range(4):  # 다음 장소 지정
        ny, nx = y + dy[k], x + dx[k]
        if 0 > nx or 0 > ny or N <= ny or M <= nx:  # 다음 장소가 arr을 벗어나면 무시
            continue
        if arr[ny][nx] == 1 and visited[ny][nx] == 0:
            DFS(ny, nx)  # 배추가 있고 방문하지 않은 지역 방문하기


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 개수
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0  # 정답 (필요 지렁이 개수)

    # 배추 위치 표시 (1)
    for k in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    # 방문하지 않은 배추 그룹 수 세기
    for y in range(N):
        for x in range(M):
            # 방문하지 않은 배추위치를 만나면 cnt를 올린다.
            if arr[y][x] == 1 and visited[y][x] == 0:
                DFS(y, x)
                cnt += 1
    print(cnt)