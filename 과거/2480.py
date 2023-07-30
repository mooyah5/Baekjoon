l = list(map(int, input().split()))
sl = list(set(l))

if len(sl) == 1:
    print(sl[0]*1000+10000)
elif len(sl) == 2:
    for i in sl:
        if l.count(i) == 2:
            print(i*100+1000)
elif len(sl) == 3:
    print(max(l)*100)