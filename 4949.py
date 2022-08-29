while True:
    S = input()
    if S == '.' and len(S) == 1:
        break
    else:
        newS = list(S.replace(' ', ''))
        q = []
        for s in newS:
            if s == '(' or s == '[':
                q.append(s)
            elif s == ')':
                if q and '(' == q[-1]:
                    q.pop(-1)
                else:
                    print('no')
                    break
            elif s == ']':
                if q and '[' in q:
                    q.pop(-1)
                else:
                    print('no')
                    break
        else:    
            if len(q)>0:
                print('no')
                break
            else:
                print('yes')