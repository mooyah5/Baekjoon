def solution(k, score):
    answer = []
    arr = []
    for i in range(len(score)):
        arr.append(score[i])    # arr에 현재 숫자 추가
        if k < len(arr):        # 단, arr에 담긴 수의 개수가 k를 초과하면
            arr.sort()              # arr을 정렬하고
            arr = arr[1:]           # 가장 작은 수를 제외해준다.
        answer.append(min(arr))   # arr의 최소값 출력
    return answer