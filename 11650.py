# # 엣날에 시간초과
# N = int(input())
# A, B = [], []
# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# for i in range(len(A)):
#     for j in range(0,len(A)-i-1):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#             B[j], B[j+1] = B[j+1], B[j]
#         if B[j] > B[j+1]:
#             B[j], B[j+1] = B[j+1], B[j]

# for i in range(len(A)):
#     print(A[i], B[i])


# 220329
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort()
for a in arr:
    print(a[0], a[1])
    