a = 'ABC'   # 3
b = 'DEF'   # 4
c = 'GHI'   # 5
d = 'JKL'   # 6
e = 'MNO'   # 7
f = 'PQRS'  # 8
g = 'TUV'   # 9
h = 'WXYZ'  # 10

phone_str = str(input())
sum = 0
for i in phone_str:
    if i in a:
        sum += 3
    elif i in b:
        sum += 4
    elif i in c:
        sum += 5
    elif i in d:
        sum += 6
    elif i in e:
        sum += 7
    elif i in f:
        sum += 8
    elif i in g:
        sum += 9
    else:
        sum += 10

print(sum)