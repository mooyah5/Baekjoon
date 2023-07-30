# 1로 만들기
# 1) 3로 나누어 떨어지면 /3
# 2) 2로 나누어 떨어지면 /2
# 3) -1

# dp를 이용한다
# dp = [0, 0, 1, 1] +... (n=인덱스 일 때 출력값)

n = int(input())
dp = [0, 0, 1, 1]
for i in range(4, n+1):
    dp.append(dp[i-1]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i]) # 3, 2 순서 노상관
print(dp[n])
