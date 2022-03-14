# 1 - 시간초과
N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
while M > 0:
    heights[-1] -= 1
    M -= 1
    heights.sort()
    if M == 0:
        break

print(max(heights))
