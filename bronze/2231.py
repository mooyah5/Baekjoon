# 분해합
# B2
# 브루트포스

# 가장 작은 생성자 구하기
# N은 생성자의 분해합 (M + M의 각 자리수의 합)

N = int(input())

# if N <= 10:
#     print(N)
# else:
#     for i in range(1, N + 1):
#         a = str(i)
#         ssum = 0
#         for j in a:
#             ssum += int(j)
#         ssum += int(a)
#         if ssum == N:
#             print(int(a))
#             break
#     else:
#         print(0)

n = int(input())
minAns = 0
for i in range(n, 0, -1):
    s = str(i)
    sum_ = 0
    for j in range(len(s)):
        sum_ += int(s[j])
    if i + sum_ == n:
        minAns = i
print(minAns)
