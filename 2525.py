## 파이썬 처음배웠을 때 코드
# h, m = map(int, input().split())
# time = int(input())

# if time + m >= 60:
#     h += (time+m)//m
#     m = (time+m)%60
#     if h >= 24:
#         h -= 24
# else:
#     m += time
# print(h, m)

## 220328

h, m = map(int, input().split())    # 시 분
plus = int(input())                 # 더할 분

mm = h*60 + m + plus                # 더해서 분단위로 맹들기

if mm >= 24*60:                     # 24시간초과 시 24시간 뺌
    print((mm-24*60)//60, (mm-24*60)%60)
else:
    print(mm//60, mm%60)
