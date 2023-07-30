# 편의점 2
# S2

# 편의점 세울 위치 고려중
# 주요 고객들의 위치를 파악하여, 거리 합을 최소로 하려 함
# 두 위치의 거리 = |x1-x2| + |y1-y2|

# 최소 거리의 합을 출력

N = int(input())        # 주요 고객들의 수
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

# 각 좌표의 중간값 구하기
x = sorted(arr, key=lambda x: x[0])[N//2][0]
y = sorted(arr, key=lambda x: x[1])[N//2][1]

answer = 0
for i in range(N):
    answer += abs(arr[i][0] - x) + abs(arr[i][1] - y)
print(answer)
