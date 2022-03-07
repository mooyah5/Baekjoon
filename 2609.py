a, b = map(int, input().split())

cd = []                             # 약수를 모아줄 리스트
for i in range(1, a+1):             # 둘 중 하나의 수를 1부터 1씩 증가
    if a % i == 0 and b % i == 0:   # 만약 그 수로 a와 b를 나누었을 때 나머지가 0이면
        cd.append(i)                # 공약수 리스트에 추가

gcd = max(cd)                       # 약수 리스트 중 가장 큰 수가 최대공약수
lcm = round(a / gcd * b)            # 최소공배수는 (a/gcd)*(b/gcd)*gcd

print(gcd)
print(lcm)

