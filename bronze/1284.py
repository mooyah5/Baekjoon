# 집 주소

# 1 = 2cm
# 0 = 4cm
# 나머지 = 3cm
# 여백 = 1cm
# 총 길이는?

arr = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    answer = 0
    N = str(input())
    if N == '0':
        break

    for n in N:
        n = int(n)
        answer += arr[n]
    answer += len(N) + 1
    print(answer)
