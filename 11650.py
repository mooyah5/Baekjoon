N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(len(A)):
    for j in range(0,len(A)-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            B[j], B[j+1] = B[j+1], B[j]
        if B[j] > B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]

for i in range(len(A)):
    print(A[i], B[i])
