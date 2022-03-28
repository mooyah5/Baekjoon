# # 1. 시간 초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = list(map(int,input().split()))
# arr2 = [list(map(int, input().split())) for _ in range(m)]
#
#
# for i in range(m):
#     ssum = 0
#     for j in range(arr2[i][0]-1, arr2[i][1]):
#         ssum += arr[j]
#     print(ssum)

# 2. 누적합 따로 저장 후 계산
#
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int,input().split()))

arr2 = []
temp = 0
for a in arr:
    temp += a
    arr2.append(temp)
arr2 = [0] + arr2

for _ in range(m):
    a, b = map(int, input().split())
    print(arr2[b]-arr2[a-1])
