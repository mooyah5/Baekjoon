# 무지성 첫시도
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

x = int(input())
cnt = 0

i = 0
j = n-1

while j < n: # i < j 도 가능
    if i == j:
        break
    if arr[i] + arr[j] == x:
        cnt += 1
        i += 1 # j -= 1 도 상관없음
    elif arr [i] + arr[j] < x:
        i += 1
    else:
        j -= 1

print(cnt)
