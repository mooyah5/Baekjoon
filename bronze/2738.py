# 두 행렬
# Bronze 5

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(2):
    for i in range(N):
        m = list(map(int, input().split()))
        for j in range(M):
            arr[i][j] += m[j]
for p in arr:
    print(*p)
