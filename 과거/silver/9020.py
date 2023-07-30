# 골드바흐의 추측
# Silver 2

# 두 수의 소수 판별 (소수 아닌 게 있으면 False)
def isPrime(x, y):
    arr = [x, y]
    for a in arr:
        for i in range(2, a):
            if a % i == 0:
                return False  # 소수가 아님
    return True


# 1. 시간초과
T = int(input())
for tc in range(T):
    N = int(input())
    primes = []                       # N의 소수쌍을 담을 배열
    if N == 4:                        # 2+2는 먼저 배제한다. (짝수 중 유일하므로)
        print('2 2')
        continue
    for i in range(3, N//2+1, 2):
        if isPrime(i, N-i):           # 홀수의 합이 될 수 있는 두 수의 소수 판별
            primes.append([i, N-i])   # 소수이면 primes 배열에 추가
    print(*primes[-1])                # 가장 마지막 값이 두 수의 차가 적음.


# 2.

T = int(input())
for tc in range(T):
    N = int(input())
    a = b = N // 2          # N의 중간 수로 시작한다.
    while a > 0:            # 두 수가 소수이면 출력하고 끝내고
        if isPrime(a, b):
            print(a, b)
            break
        else:               # 소수가 아니면 중심으로부터 1씩 멀어진다.
            a -= 1
            b += 1
