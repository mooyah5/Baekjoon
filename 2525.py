h, m = map(int, input().split())
time = int(input())

if time + m >= 60:
    h += (time+m)//m
    m = (time+m)%60
    if h >= 24:
        h -= 24
else:
    m += time
print(h, m)
