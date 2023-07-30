import sys

result = 1
for i in range(3):
    result = result * int(sys.stdin.readline())

# print(result)

arr = list(map(int, str(result)))
a = [0 for i in range(10)]
for i in arr:
    a[i] += 1

for i in a:
    print(i)

