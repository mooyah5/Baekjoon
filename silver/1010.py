# 다리 놓기
# S5

# 강 왼쪽에서 오른쪽으로 다리를 지을 거임.
# 강 왼쪽 포인트는 n, 오른쪽 포인트는 m개 있음.
# n <= m
# 서로 겹치지 않게 다리를 지을 수 있는 경우의 수


# 조합 문제
# nCr = n! / r! * (n-r)!
def facto(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


T = int(input())
for tc in range(T):
    r, n = map(int, input().split())
    cnt = facto(n) // (facto(r) * facto(n - r))
    print(cnt)
