# 1. 시간초과
# n = int(input())
# arr = list(map(int, input().split()))
# s, e = 0, n-1
# min_0 = abs(arr[0])
# min_i = []
# while s < e:
#     if arr[s] + arr[e] == 0:
#         min_i = [s,e]
#     elif arr[s] + arr[e] > 0:
#         if abs(arr[s] + arr[e]) < min_0:
#             min_0 = abs(arr[s] + arr[e])
#             min_i = [s,e]
#             e -= 1
#         else:
#             e -= 1
#     else:
#         if abs(arr[s] + arr[e]) < min_0:
#             min_0 = abs(arr[s] + arr[e])
#             min_i = [s,e]
#             s += 1
#         else:
#             s += 1

# print(arr[min_i[0]], arr[min_i[1]])



###
# 2. 야옹
n = int(input())
arr = list(map(int, input().split()))
s, e = 0, n-1
x = arr[s]
y = arr[e]
while s < e:
    if abs(x+y) > abs(arr[s]+arr[e]):
        x = arr[s]
        y = arr[e]
    
    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(x, y)