# 230612

# 입력 받기
import sys

input = sys.stdin.readline
T = int(input())
arr = [input().strip() for _ in range(T)]

# 다른 단어 위치 찾기
cnt = set()
for i in range(1, T):
    for j in range(len(arr[0])):
        if arr[i - 1][j] != arr[i][j]:
            cnt.add(j)

answer = ""
for i in range(len(arr[0])):
    if i in cnt:
        answer += "?"
    else:
        answer += arr[0][i]
print(answer)
