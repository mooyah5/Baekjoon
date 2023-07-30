# Baseball
# Bronze 3

Y = K = 0
T = int(input())
for tc in range(T):
    for i in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y > K :
        print('Yonsei')
    elif Y < K :
        print('Korea')
    else:
        print('Draw')

