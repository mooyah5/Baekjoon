import heapq
def solution(k, score):
    answer = []
    arr = []
    for s in score:
        heapq.heappush(arr, s)
        if len(arr) > k:
            heapq.heappop(arr)
        answer.append(arr[0])
    return answer