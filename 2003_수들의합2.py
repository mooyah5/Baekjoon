# # 혼자 풀어본 것 - 시간초과

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# s, e = 0, 0
# total = 0
# sol = 0 #cnt

# while e < N:
#     msum = 0
#     for i in range(s, e+1):
#         msum += arr[i]
#     if msum == M :
#         sol += 1
#         e += 1
#     elif msum > M :
#         s += 1
#     else:
#         e += 1

# print(sol)


# 야옹 투포인터 개념(연속부분수열)
n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
s, e = 0, 0
total = arr[0]
cnt = 0
while e < n:
    if total == m:
        cnt += 1
        e += 1
        total += arr[e]
    elif total > m:
        total -= arr[s]
        s += 1
    else:
        e += 1
        total += arr[e]
print(cnt)


# 20230308 혼자 재도전
N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0
ans = 0
while e < N:
    # print(s, e)
    leng = sum(arr[s:e+1])
    # print(s, e, leng)
    if leng == M:
        ans += 1
        e += 1
        # print(leng, leng == M)
    if s == N-2:
        break
    else:
        if leng < M or s == e:
            e += 1
        elif leng > M:
            s += 1
print(ans)
