# ACM호텔
# Bronze 3

# H층 W방 N번째손님
# 오는 손님 순서대로 방을 배정하는데,
# 1번 1층부터 H층까지 채우고 2번, 3번... 방번호를 높여감

# 예시
# H3, W3이라면
# 101, 201, 301, 102, 202, 302, 103, 203, 303 순서이며,
# 손님이 5번째라면 답은 202

# 1. 일일이 배열을 만들어 순서를 찾는 방식

T = int(input())    # 테스트케이스 개수
for tc in range(T):
    H, W, N = map(int, input().split())  # 층, 칸, 몇번째손님
    arr = [['' for i in range(W)] for i in range(H)]
    for i in range(H):
        a = str(i+1)
        # if i < 10:
        #     a = '0' + a
        for j in range(W):
            b = str(j+1)
            if j < 9:
                b = '0' + b
            arr[int(a)-1][int(b)-1] = a+b
    if N % H == 0:
        print(arr[H-1][N//H-1])
    else:
        print(arr[N % H - 1][N//H])


# 2 - 번호만 구하는 방식
T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    B = N // H + 1 if N % H != 0 else N // H    # 방번호 (0으로 나누어 떨어지면 방번호-1)
    A = N % H if N % H != 0 else H              # 층높이 (0으로 나누어 떨어지면 가장 높은층)
    # 방번호가 한자리수이면 앞에 '0'을 붙여준다
    print(int(str(A) + (str(B) if len(str(B)) == 2 else '0'+str(B))))
