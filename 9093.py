# 단어 뒤집기 B1
'''
입력
2
I am happy today
We want to win the first prize

출력
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
'''
T = int(input())
for tc in range(T):
    S = input().split()
    for s in S:
        print(s[::-1], end=' ')
    print()
        