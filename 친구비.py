n, m, k = map
arr = [0] + list(map) #친구비
par = [i for i in range(n+1)]
visited = [ False (n+1)]

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def union_(a, b): # c++기준 예약어 있음
    a = find(a)
    b = find(a)
    
    if a== b:
        return
    
    par[a] = b # 붙일 때(집합이 합쳐질 때 기준으로 더 싼 친구비를 저장)
    arr[b] = min(arr[a], arr[b])

for i in range(m):
    a , b = map
    
    union_(a, b)    # 트리 완성

ans = 0
for i in range(1, n+1): # 1번노드부터 차례차례
    x = find(i) # 루트의 최소값들의 합을..?
    
    if visited[x]:
        continue
    
    ans += arr[x]
    visited[x] = True

print(ans)