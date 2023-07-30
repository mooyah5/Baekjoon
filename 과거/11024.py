# 더하기 4 B3
# 수 n개의 합 출력

n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    print(sum(arr))
    