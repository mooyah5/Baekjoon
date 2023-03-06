# 약수 구하기
# 브론즈 3

# 입력
# N, K

# 출력
# N의 약수들 중 K번째로 작은 수 (약수 개수가 적으면 0)

N, K = map(int, input().split())
arr = []
for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)
if len(arr) < K:
    print(0)
else:
    print(arr[K-1])
