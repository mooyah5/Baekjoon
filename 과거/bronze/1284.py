# 집 주소
# Bronze 3

# 1 = 2cm
# 0 = 4cm
# 나머지 = 3cm
# 여백 = 1cm
# 총 길이는?

arr = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    # 0이 나오면 반복 종료
    N = str(input())
    if N == '0':
        break

    answer = len(N) + 1    # 여백
    for n in N:
        answer += arr[int(n)]
    print(answer)
