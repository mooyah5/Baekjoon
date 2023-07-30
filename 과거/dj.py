n, m ,x = map(int, input().split())
v = [list(map(int, input().split())) for i in range(n)]
rv = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())

    v[a].append([b,c]) # 정방향
    rv[b].append([a,c]) # 역방향
    
dist = [1000000000 fo ri in range(n+1)]
def get_dist(s, v): # 다익스트라
    hq = []
    dist[s] = 0
    heapq.heappush(qh, (0, s))
    while len(pq) > 0:
        d, cur = heapq.heappop(hq)
        
        if dist[cur] != d:
            continue
        
        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = d + v[cur][i][1]
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heqppush(hq, (nd, nxt))
                
        

dist = 초기화
get_dist(x, v)  # 정방향돌리기
ans = dist.copy()

dist = 초시과
fet_dist(x, rv)  # 역방향돌리기


for i in range(1, n+1):
    ans[i] += dist[i]
    
for i in range(1, n+1):
    mx = max(mx, ans[i])
    
print(mx)