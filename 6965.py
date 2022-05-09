n = int(input())

for i in range(n):
    S = list(map(str, input().split(' ')))
    for s in S:
        if len(s) == 4:
            print('****', end=' ')
        else:
            print(s, end=' ')
    print()
