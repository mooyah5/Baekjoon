# 문자메시지
# 브론즈1

# 핸드폰 자판(1~9)으로 영어 메시지를 치려고 한다.
# 걸리는 최소 시간은?

# 한 번 누른 후 일정 시간을 기다려야 한다.
# 1번 = 공백, 연속으로 누를 때 기다릴 필요 없음

# 첫째 줄: p (버튼 누르는 데 걸리는 시간), w (같은숫자부분을 연속으로 누를 때 걸리는 시간)
# 둘째 줄: 적을 문자열 S (S < len(S)), 앞뒤 공백 없음, 알파벳 대문자와 띄어쓰기만으로 구성됨

board = {
    1: ' ',
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']
}
p, w = map(int, input().split())
S = input()
arr = []
stack = []
res = 0
for s in S:
    print()
    print(s)
    if s == ' ':
        if stack[-1] == ' ':
            res += w
        res += p
        stack.append(s)
    else:
        for i in range(1, 10):
            if s in board[i]:
                if not stack:
                    stack.append(s)
                    res += p
                    continue
                if stack[-1] == s:
                    for j in range(board[i].index(s)+1):
                        res += p
                else:
                    res += p + w
                stack.append(s)
    print(stack, res)
print(res)
