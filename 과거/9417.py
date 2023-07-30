# 최대 GCD S4
# 정수 M개가 주어졌을 때 모든 두 수의 쌍 중 가장 큰 최대공약수
import math

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
for a in arr:
    yaks = []
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            x, y = a[i], a[j]
            yaks.append(math.gcd(x, y))
            # for k in range(1, max(x, y)+1):
            #     if x%k == 0 and y%k==0:
            #         yaks.append(k)
    gcd = max(yaks)
    print(gcd)

        