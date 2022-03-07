import sys

result = 1
for i in range(3):
    result *= int(sys.stdin.readline())
    
arr = [0 for i in range(10)]
for i in list(map(int, str(result))):
    arr[i] = i

for i in arr:
    print(i)

# 다시