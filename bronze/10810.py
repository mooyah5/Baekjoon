# 공 넣기
# Bronze 3

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
for m in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        arr[idx] = k
print(*arr)
