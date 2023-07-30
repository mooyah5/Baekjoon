def calc(cnt, i):
    global amount

    if amount >= cash[i]:
        amount -= cash[i]
        cnt += 1
        if amount == 0:
            cnt+=1
            return cnt
    else:
        i += 1
    calc(cnt, i)
    return cnt

N, amount = map(int, input().split())
cash = []
for _ in range(N):
    cash.append(int(input()))
cash.sort(reverse=True)

i = 0
cnt = 0
print(calc(cnt, i))
