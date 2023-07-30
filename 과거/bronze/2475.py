# 검증수
# Bronze 5

arr = list(map(int, input().split()))
narr = list(map(lambda x: x**2, arr))
print(sum(narr) % 10)
