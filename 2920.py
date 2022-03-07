import sys
a = list(map(int, sys.stdin.readline().split()))
b = [a[0]]
c = []
for i in a:
    if b[-1] > i:
        c.append('d')
        b.append(i)
    elif b[-1] < i:
        c.append('a')
        b.append(i)
    else:
        pass

if 'd' in c and 'a' in c:
    print('mixed')
elif 'd' in c:
    print('descending')
else:
    print('ascending')
    

