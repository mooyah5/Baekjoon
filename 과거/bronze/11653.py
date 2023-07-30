# 소인수분해
# Bronze 1

# 정수 N을 소인수분해

# 입력
# 1 <= N <= 10,000,000

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력
# N == 1이면 아무것도 출력하지 않음.

N = int(input())
while N > 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N //= i
            break
