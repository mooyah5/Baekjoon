# 백준 - 집합의 표현

par = [i for i  in range(1000010)]

def find_(x) : # 루트를 찾는 함수
    if par[x] == x:
        return # 내가 바로 루트
    else:
        return find_[par[x]] # 아니면 한 칸 올라가봐
    
def union_(a, b):
    a = find_(a)
    b = find_(b)
    #각자 루트까지 올라간 다음
    par[a] = b
    
n, m  = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_(b, c)
    else:
        if find_(B) == find_(c):
            print("YES")
        else:
            print("NO")
            
            
# 최적화

par = [i for i  in range(1000010)]

def find_(x) : # 루트를 찾는 함수
    if par[x] == x:
        return # 내가 바로 루트
    else:
        par[x] = find_(par[x]) ### dp 스러운 코드가 하나 더 생겼죠
        # 각 함수마다 리턴하기 전에 부모번호를 가장 이전의 것으로 바꿈...
        return par 
    
def union_(a, b):
    a = find_(a)
    b = find_(b)
    #각자 루트까지 올라간 다음
    par[a] = b
    
n, m  = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_(b, c)
    else:
        if find_(B) == find_(c):
            print("YES")
        else:
            print("NO")
            
### union by rank
par = [i for i  in range(1000010)]

def find_(x) : # 루트를 찾는 함수
    if par[x] == x:
        return # 내가 바로 루트
    else:
        par[x] = find_(par[x]) ### dp 스러운 코드가 하나 더 생겼죠
        # 각 함수마다 리턴하기 전에 부모번호를 가장 이전의 것으로 바꿈...
        return par 
    
def union_(a, b):
    a = find_(a)
    b = find_(b)
    #각자 루트까지 올라간 다음
    if rnk[a] < rnk[b]:
    
n, m  = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_(b, c)
    else:
        if find_(B) == find_(c):
            print("YES")
        else:
            print("NO")