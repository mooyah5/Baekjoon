# """
# 14247 나무자르기
# 나무 N개 한 줄을 자를 수 있는데,
# 환경을 위해 필요한 만큼만 자르고 싶다.
# 필요한 나무의 길이 M이 주어졌을 때,
# 절단기에 설정 가능한 최대 높이는 H는?
# """

# # 나의 문제 이해
# # 1) 적은 길이로 자라는 것부터 순차적으로 자른다.
# # 2) 자를 때마다 길이 늘려줌


# # 1. 시간초과

# # 입력 받아서 쌍 리스트로 만들기
# N = int(input())            # 나무의 개수 (n일 동안 자를 거임)
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# # c = list(zip(a, b))
# c = []
# for i in range(N):
#     c.append([a[i], b[i]])

# # 나무 길이 작은 인덱스 찾기
# def min_index(c):
#     min_up = c[0][1]
#     min_index = 0
#     for i in range(len(c)):
#         if c[i][1] < min_up:
#             min_up = c[i][1]
#             min_index = i
#     return min_index

# # 밤에 키 크는 나무
# def up(c):
#     for i in range(len(c)):
#         c[i][0] += c[i][1]
#     return c

# d = 0                           # 벌목한 나무 길이 합
# while c:
#     d += c[min_index(c)][0]     # 나무 자르기
#     c.pop(min_index(c))         # 자른 나무 제거
#     up(c)                       # 밤에 키 크는 나무들

# print(d)                        # 다 자르면 벌목길이 출력


# # 2. 봄봄
# '''
# 매일매일 나무가 자라므로 성장속도에 따른 정렬을 했다.
# 1. 나무의 길이는 상관이 없다. 어차피 나중에 자르든 처음에 자르든 똑같기 때문
# 2. 나무의 성장속도가 빠른 나무를 가장 나중에 골라야한다. 최대한 커달라구
# 3. 나무가 선택되었다면 (원래의 길이) + (성장속도 * 날짜) 를 해주면 통과

# * 문제에서 나무를 자른 이후에도 나무는 0부터 다시 자라기 때문에 같은
#  나무를 여러 번 자를 수는 있다. 라고 명시되어 있는데 
# 한 나무만 자르는 경우는 없는 것 같고 그런 케이스가 있다면 
# 나무의 성장속도가 3번 케이스보다 클때를 체크해주면 될듯?
# '''
# n = int(input())
# A = list(map(int, input().split()))  # 나무의 길이
# B = list(map(int, input().split()))  # 나무의 성장속도
# C = [[B[i], A[i]] for i in range(n)]
# C.sort()
# hap = 0
# for i in range(n):
#     hap += C[i][1] + C[i][0] * i
# print(hap)



## 3. 다시 풀어보기
# 자라는 키가 큰 나무들은 최대한 나중에 자르는 게 이득
n = int(input())
a = list(map(int,input().split()))  # 나무 원래 키
b = list(map(int,input().split()))  # 밤마다 자라는 키
arr = [[b[i], a[i]] for i in range(n)]
arr.sort()

tree_h = 0
for i in range(n):
    tree_h += arr[i][1] + arr[i][0] * i
print(tree_h)