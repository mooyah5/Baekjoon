# 팰린드롬인지 확인하기
# Bronze 2

# 입력: 알파벳 소문자 문자열
# 출력: 팰린드롬이면 1, 아니면 0

S = input()
ans = 1
for i in range(len(S)//2):
    if S[i] != S[len(S)-1-i]:
        ans = 0
        break
print(ans)
