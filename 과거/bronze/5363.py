# 요다 브론즈2
# 모든 문장에서 가장 앞 단어 두개를 마지막에 말한다.

T = int(input())
for tc in range(T):
    S = list(map(str, input().split()))
    print(' '.join(S[2:len(S)]), end=' ')
    print(' '.join(S[0:2]))