# 팩토리얼 2

# 0보다 큰 정수 N이 주어진다.
# N!을 출력

n = int(input())
ans = 1

for i in range(n):
    ans *= i+1
print(ans)
