n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
s, e = 0, 1
while s <= e and e <= n:
    if sum(arr[s:e]) == m:
        cnt += 1
        e += 1
    elif sum(arr[s:e]) < m or s + 1 == e:
        e += 1
    else :
        s += 1
print(cnt)