a, b = input().split()      # 상근이가 준 세자리 숫자 두개
c, d = '', ''               # 상수가 인식할 a, b => c, d

for i in range(2, -1, -1):  # 문자열로 순회해서 거꾸로 c, d에 저장
    c += a[i] 
    d += b[i]

if int(c) > int(d):
    print(int(c))
else:
    print(int(d))