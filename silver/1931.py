# 회의실배정
# S1
# 그리디, 탐욕, Greedy

# 문제
# 한 개의 회의실을 사용하고자 하는 n개의 회의들에 대한 사용시간표를 만들려고 한다.
# 각 회의에 대해 시작시간, 끝나는 시간이 주어져 있다.
# 각 회의가 겹치지 않게 하면서 가장 많은 수의 회의를 진행할 수 있도록 했을 때의 최대 회의 수는?

# 입력
# 회의 수 N이 첫줄에 들어오고, 다음부터 N줄에 걸쳐 시작시간, 끝시간이 공백으로 구분돼 입력된다.

N = int(input())
meeting = [list(map(int, input().split())) for i in range(N)]
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
end_time = 0  # 현재 회의했던 회의가 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)


# 풀이
# 가장 빨리 끝나는 회의부터 진행시키면 된다.
# 회의가 빨리 끝나는 시간부터 고르는 것이 늦게 끝나는 회의를 고르는 것보다
# 회의에 사용할 수 있는 남은 시간이 무조건 많기 때문이다.
