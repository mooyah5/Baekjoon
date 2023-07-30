import collections
N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

dict_ = collections.defaultdict(int)
for i in range(N):
    dict_[Ns[i]] = 1

for m in Ms:
    if m in dict_:
        print(1)
    else:
        print(0)