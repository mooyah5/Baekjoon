# 신입사원
# S1
# 그리디, Greedy, 탐욕 알고리즘

# 입력
# 첫째줄에 테스트케이스
# 각 테스트케이스 첫째줄에 지원자 수
# 이후로 N명의 키, 몸무게가 공백으로 구분되어 주어진다.

# 출력
# 선발 최대 인원을 출력하세용

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = sorted(arr, key=lambda x: (x[0], x[1]))
    cnt = 0
    least = 2174000000
    for a in arr:
        if a[1] < least:
            least = a[1]
            cnt += 1
    print(cnt)
