# 일곱난쟁이
# B1
# 브루트포스, 정렬, 투포인터

# 문제
# 9난쟁이 중 진또배기 7난쟁이만 찾아내기 (오름차순 출력)
# 일곱난쟁이 키의 합은 100이다. (9난쟁이 키는 모두 다름)

## 1)

# list_ = []
# for _ in range(9):
#     list_.append(int(input()))

# chas = sum(list_)-100

# for i in range(0, 8):
#     for j in range(i+1, 9):
#         if list_[i] + list_[j] == chas:
#             list_.remove(list_[j])
#             list_.remove(list_[i])
#             break
#     if len(list_) == 7:
#         break

# list_.sort()
# for i in list_:
#     print(i)

## 2) 투포인터 도전
# list_ = []
# for _ in range(9):
#     list_.append(int(input()))
# list_.sort()

# cha = sum(list_) - 100
# l = 0
# r = 8

# while l < r:
#     if list_[l] + list_[r] == cha:
#         list_.remove(list_[r])
#         list_.remove(list_[l])
#         break
#     elif list_[l] + list_[r] < cha:
#         l += 1
#     else:  # 두 포인터의 합이 cha보다 크면
#         r -= 1
#     if l > len(list_) or r < 0:
#         break

# print(list_)

## 3)
# arr = []
# for _ in range(9):
#     arr.append(int(input()))
# arr.sort()

# liers_h = sum(arr) - 100

# s, e = 0, 8
# liers_i = []
# while s < e:
#     if arr[s] + arr[e] == liers_h:
#         arr.remove(arr[e])
#         arr.remove(arr[s])
#         break
#     elif arr[s] + arr[e] < liers_h:
#         s += 1
#     else:
#         e -= 1

# for i in arr:
#     print(i)


## 4) 20230514
arr = [int(input()) for _ in range(9)]
arr.sort()
s, e = 0, 8
trash = sum(arr) - 100
while s < e and e < 9:
    if arr[s] + arr[e] < trash:
        s += 1
    elif arr[s] + arr[e] > trash:
        e -= 1
    else:
        break
for j in range(9):
    if s == j or e == j:
        continue
    print(arr[j])
