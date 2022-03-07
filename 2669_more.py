# empty = [[0 for _ in range(101)] for _ in range(101)]

# for i in range(4):
#     x1, y1, x2, y2 = map(int, input().split())

#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             empty[i][j] = 1

# cnt = 0
# for i in range(101):
#     for j in range(101):
#         if empty[i][j] == 1:
#             cnt += 1
# print(cnt)


## 소정현 - 인덱스 에러
square_dict = {}

for i in range(4):
    s = list(map(int, input().split()))
    for j in range(s[1], s[3]):
        lst = [0] * (s[2]) # 초기화 각 y값에 들어갈 list
        for k in range(s[0], s[2]):
            lst[k] = 1
        if j in square_dict.keys():
            if len(lst) > len(square_dict[j]):
                square_dict[j] += lst[len(square_dict[j]):]
            else:
                for num in range(len(square_dict[j])+1):
                    if square_dict[j][num] == 0:
                        square_dict[j][num] += lst[num]
        else:
            square_dict[j] = lst


tot = 0
for k in square_dict.values():
    tot += sum(k)

print(tot)