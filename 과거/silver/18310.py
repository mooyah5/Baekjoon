# 안테나
# S3

# 마을에 일직선상으로 집들이 위치해 있음
# 특별히 하나의 집에만 안테나 설치해주기로 함
# 효율성 위해 안테나로부터 다른 모든 집까지의 거리 총합이 최소가 되도록 설치
# (동일 위치에 여러 집이 존재할 수 있다)

# 1) 응 시간초과
# N = int(input())        # 집의 개수 (최대 20만개)
# arr = sorted(list(map(int, input().split())))   # 집 위치 (1이상 10만 이하 자연수)
# leastM = 2174000000
# leastI = 0
# for i in range(N):
#     M = 0
#     for j in range(N):
#         if i != j:
#             M += abs(arr[i] - arr[j])
#     if M < leastM:
#         leastM = M
#         leastI = arr[i]
# print(leastI)


# 2) 그냥... 수학으로
N = int(input())        # 집의 개수 (최대 20만개)
arr = sorted(list(map(int, input().split())))   # 집 위치 (1이상 10만 이하 자연수)
print(arr[((N-1)//2)])
