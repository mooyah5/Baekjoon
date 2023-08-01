def solution(board, moves):
    answer = 0
    # 1. 인형을 뽑아 스택에 모두 담는다.
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    print(stack)
    # 2. 스택에서 2개씩 중복되는 값을 제거하고 그 개수를 세어준다.
    i = 0
    while i < len(stack):
        if len(stack) > i+1 and stack[i] == stack[i+1]:
            del stack[i+1]
            del stack[i]
            answer += 2
            if i != 0:  # 인덱스가 0인 경우 후퇴하면 안돼!
                i -= 1
        else:
            i += 1
    return answer