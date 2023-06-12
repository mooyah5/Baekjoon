# N과 M (1)
# S3
# 백트래킹

# 자연수 N, M이 주어진다.
# 1부터 N까지 자연수 중, 중복없이 M개를 고른 수열을
# 사전 증가 순으로 한 줄씩 출력


def dfs():
    global arr
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if i in arr:
            continue
        arr.append(i)
        dfs()
        arr.pop()
    return


answer = []
N, M = map(int, input().split())
arr = []
dfs()
