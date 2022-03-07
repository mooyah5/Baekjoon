## 내 풀이...

# a, b = map(int,input().split())
# x, y = 0, 0
# list_ = []
# for i in range(a):
#     list_.extend(input().split())
# for i in range(a):
#     if 'X' not in list_[i]:
#         x += 1
# for j in range(b):
#     if list_[i][j] == '.':
#         yy = []
#         for k in range(a):
#             yy.append(list_[k][j])
#         if 'X' not in yy:
#             y += 1
# list_2 = [x, y]
# print(max(list_2))


## 다른 사람 풀이

n,m = map(int,input().split())
castle=[]

for _ in range(n):
    castle.append(input())

row = []
col = []

for i in range(n):
    row.append("X" not in castle[i])

for j in range(m):
    col.append("X" not in [castle[i][j] for i in range(n)])    

print(max(sum(row),sum(col)))