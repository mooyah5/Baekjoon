import heapq

n , m = map(int, input().split())
s = int(input())
v = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c]) # 양방향일 경우 밑에 더 있음
    
dist = [1000000000 for i in range(n+1)]
visited = [False for i in range(n+1)]

hq = [] # 힙큐 생성

dist[s] = 0
heapq.heappush(hq, (0, s))
while len(hq) > 0 :
# for _ in range(n):
    # mn = 10000000   # min 값을 크게 잡아놓고
    # cur = 0         # 시작점만 0으로 해놓고
    # for i in range(1, n+1):
    #     if not visited[i] and dist[i] < mn : # 방문 안했고 젤 짧은 거
    #         mn = dist[i]
    #         cur = i
    d, cur = heapq.heappop(hq)
    
    visited[cur] = True
    

    for i in range(len(v[cur])):
        # nxt = v[cur][i][0]              # 다음 노드
        # nd = dist[cur] + v[cur][i][1]   # 다음까지의 거리 (나까지의 거리)
        # if dist[nxt] > nd:              # 거리 갱신 가능할 경우(더 짧다면)
        #     dist[nxt] = nd              # 갱신한다
            heapq.heappush(hq, (nd, nxt))

for i in range(1, n+1):
    if dist[i] == 1000000000:
        print('INF')
    else:
        print(dist[i])