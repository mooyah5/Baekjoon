# 연속합
# S2


n = int(input())
arr = list(map(int, input().split()))
s, e = 0, 0
maxsum = 0
while s < e:
    asum = 0
    for i in range(s, s + e + 1):
        asum += arr[i]
    if asum > maxsum:
        maxsum = asum
    if arr[e + 1] > 0:
        e += 1
    elif arr[s] <= 0:
        s += 1
    e += 1
print(maxsum)
