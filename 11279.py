N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
    print(arr.pop(max(arr)))