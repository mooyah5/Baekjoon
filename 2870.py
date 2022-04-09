# 수학숙제 S4

n = int(input())
num = ['0','1','2','3','4','5','6','7','8','9']
arr = []
for i in range(n):
    S = input()
    tmp = ''
    for s in S:
        if s in num:
            tmp += s
        else:
            if tmp:
                arr.append(int(tmp))
                tmp = ''
    if tmp:
        arr.append(int(tmp))
arr.sort()
for a in arr:
    print(a)