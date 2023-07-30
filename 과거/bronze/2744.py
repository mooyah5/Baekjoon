# 대소문자 바꾸기
# Bronze 5

S = input()
ans = ''
for s in S:
    if s.isupper():
        ans += s.lower()
    else:
        ans += s.upper()
print(ans)
