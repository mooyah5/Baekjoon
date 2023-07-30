# 용액
# G5
# 이분탐색, 투포인터

# 문제
# 용액 개수 N이 첫줄에 들어오고
# 두번째 줄에 용액들의 특성값이 공백으로 구분, 정렬되어 들어온다.
# 혼합하여 0에 가장 가까운 용액을 만드는 두 용액을 찾아라

# 출력
# 오름차순으로 출력하며, 두 경우 이상이면 아무거나 하나 출력한다.


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
# 2.
# n = int(input())
# arr = list(map(int, input().split()))
# s, e = 0, n - 1
# x = arr[s]
# y = arr[e]
# while s < e:
#     if abs(x + y) > abs(arr[s] + arr[e]):
#         x = arr[s]
#         y = arr[e]

#     if arr[s] + arr[e] < 0:
#         s += 1
#     else:
#         e -= 1

# print(x, y)


# 3. 20230514
def Two_Pointer(s, e):
    global ans
    while s < e and e < N:
        mixed = arr[s] + arr[e]
        if abs(mixed) < abs(ans[0]):
            ans = [mixed, s, e]
        if mixed > 0:
            e -= 1
        elif mixed < 0:
            s += 1
        else:  # 0과 일치하면
            print(arr[ans[1]], arr[ans[2]])
            return
    print(arr[ans[1]], arr[ans[2]])
    return


N = int(input())
arr = list(map(int, input().split()))
s, e = 0, N - 1
ans = [2174000000, -1, 1]  # [최소차이, s, e]
Two_Pointer(s, e)
