# 1. 아스키코드 이용
n = int(input())
for i in range(n):
    S = list(input())
    if not (65 <= ord(S[0]) <= 90): # 대문자가 아니면
        S[0] = chr(ord(S[0]) - 32)  # 아스키코드 -32 (소->대)
    print(''.join(S))
    

# 2. 첫글자 upper
n = int(input())
for i in range(n):
    S = list(input())
    S[0] = S[0].upper()
    print(''.join(S))
    # capitalize로 하면, 첫글자만 대문자가 되고, 나머지 뒷부분은 다 소문자로 바뀜