# 거품정렬

# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))

# for i in range(N-1, -1, -1):
#     for j in range(0,i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# for a in arr:
#     print(a)

##
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

for i in range(N):
    for j in range(0,N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for a in arr:
    print(a)