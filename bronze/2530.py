# 인공지능 시계

t, m, s = map(int, input().split(' '))
d = int(input())

time = (60*60*t) + (60*m) + s   # 모든 시간을 초로 변경
ans = time + d                  # 초로 변경된 시간에 추가시간을 추가
T, Tx = ans // 3600, ans % 3600  # 한시간에 해당하는 초로 나누어 시와 분초로 분리
M, S = 0, 0                     # 분, 초 초기화
if Tx:                          # 분초에 해당하는 시간이 존재할 경우, 60초로 나누어 분리
    M, S = Tx // 60, Tx % 60

if T >= 24:                     # 시가 24시를 넘어갈 경우 24로 나눈 나머지로 계산
    T = T % 24
print(T, M, S)
