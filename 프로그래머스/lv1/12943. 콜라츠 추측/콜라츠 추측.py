def solution(num):
    answer = 0
    def CollatzGuess(n, cnt):
        cnt += 1
        if cnt >= 501:
            return -1
        if n == 1:
            return cnt-1
        if n % 2 == 0:
            return CollatzGuess(n // 2, cnt)
        else:
            return CollatzGuess(n * 3 + 1, cnt)
    
    return CollatzGuess(num, 0)