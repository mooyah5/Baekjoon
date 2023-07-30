SumOfPrice = int(input())
N = int(input())
for i in range(N):
    a, b = map(int, input().split(' '))
    SumOfPrice -= a*b
if SumOfPrice == 0:
    print('Yes')
else:
    print('No')
