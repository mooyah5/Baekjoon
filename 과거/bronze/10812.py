# 바구니 순서 바꾸기
# Bronze 2
# 단계별로 풀어보기 - 2차원 배열

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for m in range(M):
    s, e, k = map(int, input().split())
    arr[s-1:e] = arr[k-1: e] + arr[s-1: k-1]
print(*arr)
