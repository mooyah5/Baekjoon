# 종이자르기 (알고리즘 추천)

x, y = map(int, input().split())
T = int(input())
xy = []
for i in range(T):
    xy.append(list(map(int, input().split())))

y_0 = []
x_1 = []
for i in range(T):
    if xy[i][0] == 0:
        y_0.append(xy[i][1])
    else: #1
        x_1.append(xy[i][1])

#최댓값만 냄기기
# max_y_0 = y_0[0]
# for i in range(1, len(y_0)):
#     if max_y_0 < y_0[i]:
#         max_y_0 = y_0[i]
# max_x_1 = x_1[0]
# for i in range(1, len(x_1)):
#     if max_x_1 < x_1[i]:
#         max_x_1 = x_1[i]

x -= max_x_1
y -= max_y_0

print(x*y)


#ㅅ