s = input().upper()
list_ = list(set(s))
cnt = []
for i in list_:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(list_[cnt.index(max(cnt))])