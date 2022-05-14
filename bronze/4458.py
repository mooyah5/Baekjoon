n = int(input())
for i in range(n):
    S = list(input())
    S[0] = S[0].upper()
    # for s in S:
    #     print(s, end='')
    # print()
    print(''.join(S))