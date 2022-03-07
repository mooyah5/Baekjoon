import sys
a, b = (map(list, sys.stdin.readline().split()))
a = list(map(int, a))
b = list(map(int, b))
# sum = 0
# for i in a:
#     for j in b:
#         sum += i*j
# 아... 이것은 sum(a)*sum(b)와 같다...
print(sum(a)*sum(b))
