# silver 1

S = list(map(int, input().split()))
top = S[0]
start = point = S[1]
end = S[2]
up = S[3]
down = S[4]
ans = past = 0

while 0 < start <= top:
    if start == end:
        print(ans)
        break
    elif point < end:
        point += up
    elif point > end:
        point -= down

    past = point
