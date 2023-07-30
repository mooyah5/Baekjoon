N, M = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
mmin = 1000000000
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if i != j and j != k and k != i:
                if (c[i]+c[j]+c[k]) <= M and M-(c[i]+c[j]+c[k]) < mmin:
                    ans = c[i]+c[j]+c[k]
                    mmin = M-(c[i]+c[j]+c[k])
print(ans)
