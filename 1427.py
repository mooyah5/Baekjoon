S = input()
N = []
for s in S:
    N.append(int(s))
    
for i in range(len(N)):
    for j in range(0,len(N)-i-1):
        if N[j] < N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]

for n in N:
    print(n, end='')