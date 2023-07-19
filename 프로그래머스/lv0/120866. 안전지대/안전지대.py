def solution(board):
    answer = 0
    # 8방향(좌우상하대각선)
    di = [-1, 1, 0, 0, -1, 1, 1, -1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            
            if board[i][j] == 1:
                # 숫자 1을 발견하면 주위를 둘러싼 8지점을 돈다.
                for k in range(8):
                    ni, nj = i + di[k], j + dj[k]

                    # 해당 지점이 유효한 지점에 있고, 0이라면 2(암거나)로 바꿔준다.
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                        board[ni][nj] = 2
                    else:
                        continue

    # 0인 부분의 개수를 구한다.
    for b in board:
        answer += b.count(0)
    return answer