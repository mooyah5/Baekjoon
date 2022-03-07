# 다시해라

minute, min_h, max_h, Tr, Re = map(int, input().split())
cnt = 0
cnt_minus = minute
now = min_h
while True:
    if max_h > now > min_h:
        now += Tr
        cnt += 1
        cnt_minus -= 1
    elif max_h <= now:
        now -= Re
        cnt_minus -= 1
    elif min_h >= now:
        now = min_h
        cnt_minus -= 1
    elif cnt_minus <= 0:
        print(cnt)
        break
    elif 
        
        
