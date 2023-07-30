import sys
while True:
    try:
        n, k = map(int, sys.stdin.readline().split())
        sum = n
        while n >= k:
            sum += n//k
            n = n//k + n%k
        print(sum)
    except:
        break