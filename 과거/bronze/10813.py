# 공 바꾸기
# Bronze 2

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
print(arr)
for m in range(M):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    arr[i], arr[j] = arr[j], arr[i]
    print(m, arr)
print(*arr)
