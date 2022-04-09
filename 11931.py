import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]
# print(arr)
arr.sort(reverse=True)
for a in arr:
    print(a)

