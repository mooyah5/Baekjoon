# 입력 : this is a test
# 출력 : CAse # 1: text a is this

T = int(input())
for tc in range(1, T+1):
    S = input().split()
    print(f'Case #{tc}:', end=' ')
    for i in range(len(S)-1,-1,-1):
        print(S[i], end=' ')