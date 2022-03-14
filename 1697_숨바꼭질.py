### 1
# N, K = map(int, input().split())
# cnt = 0
# cha = abs(N-K)
# jegop = 0
# while True:
#     if 2**jegop <= cha:
#         jegop += 1
#     else:
#         jegop -= 1
#         cha - 2**jegop
#         break

# print(jegop)
# print(cha)
# dk 이게 아니구나




### 2
# 현위치에서 두 배 하거나
# 한 칸 움직이거나
# x+1, x-1, x*2 3가지 방법으로 bfs





# deque
'''
deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
'''

# 구글링조차 이해하지 못했다.
from collections import deque

def bfs():
    q = deque()
    q.append(n)         # => q = deque([n]) 시작점 저장
    
    while q:                # q에 값이 없어질 때까지 반복
        x = q.popleft()         # 시작점 꺼내고 데크에 빈리스트만
        if x == K:              # 만약 선입값이 
            return d[x]
        for nx in [x-1, x+1, x*2]:              # nx는 세가지 이동방식을 순회
            if 0 <= nx < max_ and d[nx] == 0:   # 만약 이동했을 때 유효하고 방문하지 않았으면
                d[nx] = d[x] + 1                    # 방문체크(지점에 방문한 횟수 저장)
                q.append(nx)

N, K = map(int, input().split())
max_ = 100001 # 최대 나무길이
d = [0] * max_
print(bfs())