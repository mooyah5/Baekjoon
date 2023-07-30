# bubble X

T = int(input())
arr = []
for i in range(T):
    arr.append(int(input()))

for i in range(T-1):
    for j in range(T-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(len(arr)):
    print(arr[i])

###

# 이분탐색
T = int(input())
arr = []
for i in range(T):
    arr.append(int(input()))
center = len(arr)//2
while True:
    if arr[center]
