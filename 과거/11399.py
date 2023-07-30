# ATM

# 오름차로 정렬하면 최소가 나올 것 같다. 맞았다.

N = int(input())
arr = sorted(list(map(int, input().split())))

# 앞에서부터 N-i를 곱한 값끼리 더하면 됨
ans = 0
for i in range(0, N):
    ans += arr[i] * (N-i)
print(ans)
