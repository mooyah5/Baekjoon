import sys

data = [0 for i in range(10)]
for i in range(10):
    data[i] = int(sys.stdin.readline())

a = [0 for i in range(10)]
for i in range(len(data)):
    a[i] = data[i] % 42

print(len(list(set(a))))
