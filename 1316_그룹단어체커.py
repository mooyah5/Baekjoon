N = int(input())
strings = []
for i in range(N):
    strings.append(input())

cnt = len(strings)
for s in strings:
    q = [s[0]]                  # 첫글자를 큐에 넣고
    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i+1] not in q:
            q.append(s[i+1])
        elif s[i] != s[i+1] and s[i+1] in q:
            cnt -= 1
            break
        else:
            pass
print(cnt)