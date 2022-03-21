import sys
s = sys.stdin.readline()
cnt = 0
i = 0
while i < len(s):
    if s[i] == 'c':
        if s[i+1] == '=' or s[i+1] == '-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    elif s[i] == 'd':
        if s[i+1:i+3] == 'z=':
            cnt += 1
            i += 3
        elif s[i+1] == '-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    elif s[i] == 'l':
        if s[i+1] == 'j' :
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    elif s[i] == 'n':
        if s[i+1] == 'j' :
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    elif s[i] == 's':
        if s[i+1] == '=' :
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    elif s[i] == 'z':
        if s[i+1] == '=' :
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
        continue
    else:
        cnt +=1
        i += 1
        continue

print(cnt)