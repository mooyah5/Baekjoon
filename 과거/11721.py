S = input()
i = 0
while i < len(S):
    print(S[i], end='')
    i += 1
    if i % 10 == 0:
        print()