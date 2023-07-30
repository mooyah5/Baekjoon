# 소수
# Silver 5

# M 이상 N 이하 자연수 중 소수인 것들의 합과 최솟값
# 소수가 없으면 -1 출력

M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):         # i는 M이상 N이하 자연수들
    decimals = []               # i의 약수들을 넣을 배열
    for j in range(1, i+1):       # 1부터 i까지의 숫자 중
        if i % j == 0:            # 0으로 나누어 떨어지면 약수
            decimals.append(j)
    if len(decimals) == 2:      # i의 약수의 개수가 2개이면 i는 소수
        arr.append(i)

if len(arr) < 1:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
