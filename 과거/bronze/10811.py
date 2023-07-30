# 바구니 뒤집기
# Bronze 2

# 바구니 총 N개 (1~N 번)
# M회바구니의 순서를 i번부터 j번까지의 바구니를 역순으로 변경

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for m in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
print(*arr)
