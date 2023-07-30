# 강의실 배정
# G5
# 그리디

# N개의 수업을 최소의 강의실을 사용해서 가능하게 해야 한다. (겹치지 않게 배정)

# 입력으로 N줄만큼 각 강의 시작시간, 끝시간이 주어진다.
# 강의실 개수를 출력하라

# 풀이방법
# 1) 현 강의실에서 강의 끝시간보다 다음회의 시작시간이 빠르면 회의실 1개 추가
# 2) 현 회의실에서 강의 끝시간보다 다음회의 시작시간이 느리면 현 회의실에서 이어서 개최
import heapq  # 우선순위큐: push할때마다 정렬상태 유지

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
room = []
heapq.heappush(room, arr[0][1])  # 큐에 첫 강의 끝 시간을 넣어두고 시작
cnt = 1
for i in range(1, N):
    if arr[i][0] < room[0]:  # 현 강의 시작시간이 이전 강의 끝시간보다 빠르면
        heapq.heappush(room, arr[i][1])
    else:  # 현 강의 시작시간이 이전 강의 끝시간과 같거나 그보다 느리면 이어서 진행
        # 이전강의 끝시간을 현강의 끝시간으로 갱신
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
print(len(room))
