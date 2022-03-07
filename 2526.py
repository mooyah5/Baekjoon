import sys

# n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(9)]

max_data = 0
max_aa = 0

for i in range(9):
    if max_data < int(data[i]):
        max_data = int(data[i])
        max_aa = i+1
print(max_data)
print(max_aa)


# 첫째줄 : 최댓값
# 둘째줄 : 최댓값 몇번째수 : 