n = int(input())
arr = list(map(int,input().split()))
p = int(input())

if p in arr:
    print('답은', 0)
else:
    cnt = 0
    arr.append(p)
    arr.sort()
    point = arr.index(p)
    if point == 0:
        b = arr[1]
        for i in range(p, b):
            print(arr)
            cnt += 1
    else:
        a = arr[point-1]
        b = arr[point+1]

        for i in range(a+1, p+1):
            for j in range(i+1, b):
                print(i, j, end='/')
                cnt+=1
    print('답은', cnt)