
# 백준 최소 스패닝 트리

def find():
    pass

def union_():
    pass

n, m =map
v = [list(map(int, input().split() for i i n range(m)))]
par = [i for i in range(n+1)]

v.sort(key=lambda x:x[2])

ans = cnt = 0
for i in range(m): # 양끝이 같은 연결요소면 암것두안하고,
    x, y = v[i][0], v[i][1]
    
    if find(x) == find(y):
        continue

    union_(x, y)
    ans += v[i][2]
    cnt += 1
    
print(ans)    

### 문제응용(백준-행성터널) - 간선이 n-1이면 트리죠
if cnt == n-1:
    pass # 트리다
else:
    pass # 트리 아니다
    
