# 듣보잡
# 듣지도, 보지도 못한 사람의 명단 구하기

# n, m
# n 줄에 듣지못한 사람이름
# m 줄에 보지 못한 사람 이름

# 입력
'''
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''

# 출력
'''
2
baesangwook
ohhenrie
'''

## 1 - 시간초과

# n, m = map(int, input().split())
# heard = []
# seen = []
# didnt = []
# for i in range(n):
#     heard.append(input())
# for i in range(m):
#     seen.append(input())
# for i in range(n):
#     if heard[i] in seen:
#         didnt.append(heard[i])
# didnt.sort()
# print(len(didnt))
# for d in didnt:
#     print(d)
    
    
## 2
n, m = map(int, input().split())
set_a = set()
set_b = set()
for i in range(n):
    set_a.add(input())
for i in range(m):
    set_b.add(input())

res = list(set_a & set_b)
res.sort()
print(len(res))
for r in res:
    print(r)