# 숫자 카드
# Silver 5

# 1. 시간초과
# N = int(input())
# Narr = list(map(int, input().split()))
# M = int(input())
# Marr = list(map(int, input().split()))
# for m in Marr:
#     if m in Narr:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


# 2. 시간 안 된다 싶으면 딕셔너리
N = int(input())
Narr = list(map(int, input().split()))
M = int(input())
Marr = list(map(int, input().split()))
dic = dict()
for n in Narr:
    dic[n] = 1

for m in Marr:
    if m in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')
