def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    return sorted(answer) if len(answer) else [-1]
    # return answer