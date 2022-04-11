n, m = map(int, input().split())
arr = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = j+i*m+1
    #     print(j+i*m+1, end=' ')
    # print()
for a in arr:
    print(*a)