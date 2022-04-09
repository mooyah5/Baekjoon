price, cnt, money = map(int, input().split())
sum_price = price * cnt
if sum_price > money:
    print(sum_price-money)
else:
    print(0)