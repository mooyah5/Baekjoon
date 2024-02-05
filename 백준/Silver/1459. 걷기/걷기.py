# 240205

x, y, w, s = map(int, input().split())
go_straight = (x+y) * w
go_diagonal = (max(x,y)-1) * s + w if (x+y)%2 else max(x,y) * s
go_hybrid = min(x, y) * s + abs(x-y) * w

print(min(go_straight, go_diagonal, go_hybrid))