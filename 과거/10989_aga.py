# N = int(input())
# arr = []
# arr2 = [0 for i in range(N)]
# for _ in range(N):
#     arr.append(int(input()))
# for i in range(N):
#     arr2[arr[i]] += 1
#
# for i in arr2:
#     print(arr[i])

import sys
N = int(sys.stdin.readline())
nums = [0]* 10001
arr = []
for i in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
