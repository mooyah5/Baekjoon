# 좋은 단어 (큐)

T = int(input())
res = 0
for tc in range(T):
    S = input()
    q = []
    for s in S:
        if len(q) >= 1 and s == q[-1] :
            q.pop(-1)
        else:
            q.append(s)
    if len(q) == 0:
        res += 1
print(res)