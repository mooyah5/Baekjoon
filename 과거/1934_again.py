T = int(input())
list_ = [[] for _ in range(T)]
for i in range(T):
    list_[i].extend(map(int,input().split()))

cd = [[] for i in range(T)]

for i in range(len(list_)):
    for j in range(1, list_[i][0]+1):
        if list_[i][0] % j == 0 and list_[i][1] % j == 0:
            cd[i].append(j)

print(cd)
# max_ = [list_[i][0] * list_[i][1] for i in range(len(list_))]



# print(max_)