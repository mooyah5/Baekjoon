# 숫자 카드 2
# silver 4
# 230613

## 문제
# 정수 하나 적힌 숫자카드가 주어진다.
# N개의 숫자카드 중, M개의 숫자카드에 적힌 수가 몇개나 있는지 M개씩 각각 출력

## 입력 설명
# N (숫자카드 개수)
# N개의 숫자카드에 적힌 수가 공백으로 나뉘어 입력
# M
# M개의 숫자카드에 적힌 수가 공백으로 나뉘어 입력

## 입력
n = int(input())
N_arr = list(map(int, input().split()))
m = int(input())
M_arr = list(map(int, input().split()))

# ## 1. 시간초과
# arr = [0 for _ in range(m)]

# for i in range(m):
#     for N in N_arr:
#         if M_arr[i] == N:
#             arr[i] += 1

# for a in arr:
#     print(a, end=" ")

## 2. 해쉬 알고리즘
hashmap = dict()
for N in N_arr:
    if N in hashmap:
        hashmap[N] += 1
    else:
        hashmap[N] = 1

arr = [0 for _ in range(m)]
for i in range(m):
    if M_arr[i] in hashmap:
        arr[i] = hashmap[M_arr[i]]
print(" ".join(str(arr[i]) for i in range(m)))
