res = [[-1] * 15 for i in range(15)]

for i in range(5):
    S = list(input())
    for j in range(len(S)):
        res[i][j] = S[j]

for j in range(15):
    for i in range(15):
        if res[i][j] != -1:
            print(res[i][j], end='')