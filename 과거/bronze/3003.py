# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 1,  1,  2,    2,      2, 8

# list_ = list(map(int, input().split()))
# val = [1, 1, 2, 2, 2, 8]
# pm = []
# for i in range(6):
#     if list[i] != val[i]:
#         pm.append(val[i]-list_[i])
#     else:
#         pm.append(0)
# for i in pm:
#     print(i, end=' ')


# 2023 03 04 재도전
arr = [1, 1, 2, 2, 2, 8]
ans = [0 for i in range(6)]
lst = list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] == arr[i]:
        continue
    else:
        if lst[i] > arr[i]:
            ans[i] = arr[i] - lst[i]
        else:
            ans[i] = arr[i] - lst[i]

print(" ".join(map(str, ans)))
