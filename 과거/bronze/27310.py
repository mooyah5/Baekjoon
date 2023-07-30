# Bronze 4
# :chino_shock:

# 이모지 난이도 계산
# 이모지 전체길이 + 콜론개수 + 언더바 개수 * 5
# 예) chino_shock: 13+2+1*5-20

Colons = 0
UnderBar = 0

S = str(input())
for i in range(len(S)):
    if S[i] == ':':
        Colons += 1
    elif S[i] == '_':
        UnderBar += 1

print(Colons+len(S)+UnderBar*5)
