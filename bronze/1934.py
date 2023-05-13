# 최소공배수
# 2023-03-10

# A, B의 최소공배수를 구하라

# 1. 시간초과
# N = int(input())
# for n in range(N):
#     A, B = map(int, input().split())
#     for i in range(max(A, B), (A*B)+1):
#         if i % A == 0 and i % B == 0:
#             print(i)
#             break

# 2.
N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    if B > A:
        A, B = B, A
    X, Y = A, B
    while A % B != 0:
        A = B
        B = A % B
    print(X * Y // B)
