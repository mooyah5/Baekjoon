n = int(input())
if n % 2 == 0: #짝수
    print((n/2+1)**2)
else: #홀수
    print(int((n+1)*(n+3)/4))
