N = int(input())
strings = []
for i in range(N):
    strings.append(input())

cnt = len(strings)
for s in strings:
    q = [s[0]]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] in q:
                cnt -= 1
                break
        else:
            pass
print(cnt)