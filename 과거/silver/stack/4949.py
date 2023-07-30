while True:
    S = input()
    ans = "yes"
    if S == '.' and len(S) == 1:
        break
    else:
        newS = list(S.replace(' ', ''))  # 공백 없애기
        q = []
        for s in newS:
            if s == '(' or s == '[':
                q.append(s)
            else:
                if s == ')':
                    if not q or q.pop() != '(':
                        ans = 'no'
                elif s == ']':
                    if not q or q.pop() != '[':
                        ans = 'no'
                if ans == 'no':
                    break
        if q or ans == 'no':
            print('no')
        else:
            print('yes')
