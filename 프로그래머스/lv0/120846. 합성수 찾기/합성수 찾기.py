def solution(n):
    answer = 0
    for num in range(4, n+1):
        for j in range(2, num):
            if num % j == 0:
                answer += 1
                break
    return answer